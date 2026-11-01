#pragma once

// GraphApi — 노드 그래프 C API 브릿지(엔진 그래프 편집기는 호스트 창에서 안 그려져 C API 로 같은 일을 한다).
//
// 노드를 넣고(CAD_NodeGraphAddNode) 입력 값을 넣고(CAD_NodeGraphSet*) 이으면(CAD_NodeGraphConnect) 엔진이 다음 프레임에
// 계산해 output 노드가 장면 객체를 만든다. 굽기(CAD_NodeGraphBake)는 그 객체를 그래프에서 떼어 보통 객체로 남긴다.
// ⚠️ 종류 목록(CAD_NodeGraphGetKindsJson)은 엔진이 한 프레임 돈 뒤에 묻는다 — 그 전엔 엔진이 죽는다. 패널을 처음 열 때 읽는다.
// ⚠️ CAD_ClearAll 은 다음 프레임에 그래프까지 지운다.

#include "cad_json.h"

#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QObject>
#include <QString>
#include <QStringList>
#include <QVariantList>
#include <QVariantMap>
#include <QtQml/qqmlregistration.h>

#include <algorithm>
#include <vector>

class GraphApi : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    Q_PROPERTY(QVariantList kinds READ kinds NOTIFY kindsChanged)   // [{kind,group,inputs:[{name,type}],outputs:[{name,type}]}]
    Q_PROPERTY(QVariantList nodes READ nodes NOTIFY changed)        // [{id,kind,state,inputs,outputs}] — 화면에 보일 것만 모아서
    Q_PROPERTY(QString summary READ summary NOTIFY changed)
    Q_PROPERTY(QString message READ message NOTIFY messageChanged)

public:
    explicit GraphApi(QObject* parent = nullptr) : QObject(parent) {}

    QVariantList kinds() const { return kinds_; }
    QVariantList nodes() const { return nodes_; }
    QString summary() const    { return summary_; }
    QString message() const    { return message_; }

    Q_INVOKABLE void loadKinds() {
        if (!kinds_.isEmpty()) return;
        kinds_ = QJsonDocument::fromJson(cadjson::readBytes(&CAD_NodeGraphGetKindsJson)).array().toVariantList();
        emit kindsChanged();
    }

    Q_INVOKABLE void refresh() {
        const QJsonObject st = QJsonDocument::fromJson(cadjson::readBytes(&CAD_NodeGraphGetJson)).object();
        const QJsonObject g = st.value("graph").toObject();
        QMap<int, QString> errors;
        for (const auto& e : st.value("errors").toArray()) errors[e.toObject().value("id").toInt()] = e.toObject().value("error").toString();
        QSet<int> waiting;
        for (const auto& w : st.value("waiting").toArray()) waiting.insert(w.toInt());
        QSet<QString> linked;   // "노드:포트" — 이어진 입력
        for (const auto& l : g.value("links").toArray())
            linked.insert(QString("%1:%2").arg(l.toObject().value("to").toInt()).arg(l.toObject().value("toPort").toString()));

        QVariantList nodes;
        for (const auto& v : g.value("nodes").toArray()) {
            const QJsonObject n = v.toObject();
            const int id = n.value("id").toInt();
            const QVariantMap kind = kindOf(n.value("kind").toString());
            const int objs = n.value("sceneIds").toArray().size();
            const QString state = errors.contains(id) ? "오류: " + errors[id] : waiting.contains(id) ? "입력 기다림"
                                : objs ? QString("객체 %1개").arg(objs) : QString();
            QVariantList inputs;
            for (const auto& in : kind.value("inputs").toList()) {
                QVariantMap m = in.toMap();
                m["linked"] = linked.contains(QString("%1:%2").arg(id).arg(m.value("name").toString()));
                inputs.append(m);
            }
            nodes.append(QVariantMap{{"id", id}, {"kind", n.value("kind").toString()}, {"state", state},
                                     {"inputs", inputs}, {"outputs", kind.value("outputs")}});
        }
        const QString summary = QString("노드 %1개 · 링크 %2개 · 장면 객체 %3개%4").arg(nodes.size())
            .arg(g.value("links").toArray().size()).arg(st.value("objects").toArray().size())
            .arg(st.value("pending").toBool() ? "  (계산 대기)" : "");
        objects_.clear();
        for (const auto& o : st.value("objects").toArray()) objects_.push_back(uint32_t(o.toInt()));
        if (nodes == nodes_ && summary == summary_) return;
        nodes_ = nodes; summary_ = summary;
        emit changed();
    }

    Q_INVOKABLE int addNode(const QString& kind) {
        uint32_t id = 0;
        if (!check(CAD_NodeGraphAddNode(kind.toUtf8().constData(), nextX_, 0.0, &id), "노드 넣기")) return -1;
        nextX_ += 220.0;   // 엔진 그래프 편집기에서 열어도 겹치지 않게 옆으로
        return int(id);
    }
    // type 에 맞춰 값을 넣는다 — number·integer = 숫자, bool = 참/거짓, point = "x,y,z", text = 글
    Q_INVOKABLE bool setValue(int node, const QString& port, const QString& type, const QString& text) {
        const QByteArray p = port.toUtf8();
        bool ok = true;
        CAD_Status st = CAD_E_INVALID_ARG;
        if (type == "number" || type == "integer") {
            const double v = text.toDouble(&ok);
            if (ok) st = CAD_NodeGraphSetNumber(uint32_t(node), p.constData(), v);
        } else if (type == "bool") {
            st = CAD_NodeGraphSetBool(uint32_t(node), p.constData(), QStringList{"1", "true", "참", "on", "yes"}.contains(text.trimmed().toLower()));
        } else if (type == "point") {
            const QStringList xyz = text.split(',');
            ok = xyz.size() == 3;
            if (ok) st = CAD_NodeGraphSetPoint(uint32_t(node), p.constData(), CAD_GeVec3{xyz[0].toDouble(), xyz[1].toDouble(), xyz[2].toDouble()});
        } else if (type == "text") {
            st = CAD_NodeGraphSetText(uint32_t(node), p.constData(), text.toUtf8().constData());
        } else {
            say("objects 입력은 값이 아니라 다른 노드의 출력을 잇는다");
            return false;
        }
        if (!ok) { say(QString("'%1' 는 %2 값이 아닙니다").arg(text, type)); return false; }
        return check(st, "값 넣기");
    }
    Q_INVOKABLE bool connectPorts(int from, const QString& fromPort, int to, const QString& toPort) {
        return check(CAD_NodeGraphConnect(uint32_t(from), fromPort.toUtf8().constData(), uint32_t(to), toPort.toUtf8().constData()), "잇기");
    }
    Q_INVOKABLE void disconnectPort(int to, const QString& toPort) { check(CAD_NodeGraphDisconnect(uint32_t(to), toPort.toUtf8().constData()), "끊기"); }
    Q_INVOKABLE void removeNode(int id) { check(CAD_NodeGraphRemoveNode(uint32_t(id)), "노드 지우기"); }
    Q_INVOKABLE void clear() { nextX_ = 0.0; check(CAD_NodeGraphClear(), "지우기"); }
    Q_INVOKABLE void evaluate() {
        const int32_t bad = CAD_NodeGraphEvaluate();   // 반환 = 오류 난 노드 수
        say(bad == 0 ? "계산: 오류 없음" : bad > 0 ? QString("계산: 오류 노드 %1개").arg(bad) : "계산 실패: " + cadjson::lastError());
    }
    // 그래프 객체 중 선택한 것만 — 선택이 없으면 그래프 객체 전부(0개를 넘기면 엔진은 지금 선택을 쓴다)
    Q_INVOKABLE void bake() {
        refresh();
        std::vector<uint32_t> picked;
        const int32_t n = CAD_GetSelection(nullptr, 0);
        std::vector<uint32_t> sel(size_t(n > 0 ? n : 0));
        if (n > 0) CAD_GetSelection(sel.data(), uint32_t(n));
        for (uint32_t id : sel) if (std::find(objects_.begin(), objects_.end(), id) != objects_.end()) picked.push_back(id);
        if (picked.empty()) picked = objects_;
        if (picked.empty()) return say("굽기: 그래프가 만든 객체가 없습니다");
        const int32_t made = CAD_NodeGraphBake(picked.data(), uint32_t(picked.size()), nullptr, 0);
        say(made >= 0 ? QString("굽기: %1개를 보통 객체로").arg(made) : "굽기 실패: " + cadjson::lastError());
    }
    // 예제 — 상자 → 선형 배열(5개, X 로 150) → 출력. 배열 노드의 count 를 바꾸면 장면의 상자들이 따라 바뀐다
    Q_INVOKABLE void example() {
        CAD_NodeGraphClear();
        uint32_t box = 0, arr = 0, out = 0;
        CAD_NodeGraphAddNode("box", 0, 0, &box);
        CAD_NodeGraphAddNode("array.linear", 220, 0, &arr);
        CAD_NodeGraphAddNode("output", 440, 0, &out);
        nextX_ = 660.0;
        CAD_NodeGraphSetNumber(box, "width", 100.0);
        CAD_NodeGraphSetNumber(arr, "count", 5);
        CAD_NodeGraphSetPoint(arr, "offset", CAD_GeVec3{150.0, 0.0, 0.0});
        CAD_NodeGraphSetText(out, "name", "상자 배열");
        if (check(CAD_NodeGraphConnect(box, "solid", arr, "objects"), "잇기") && check(CAD_NodeGraphConnect(arr, "objects", out, "objects"), "잇기"))
            say("예제: 상자 → 선형 배열(5개) → 출력 — 배열 노드의 count 를 바꿔 보세요");
    }

signals:
    void kindsChanged();
    void changed();
    void messageChanged();

private:
    QVariantMap kindOf(const QString& kind) const {
        for (const auto& k : kinds_) if (k.toMap().value("kind").toString() == kind) return k.toMap();
        return {};
    }
    bool check(CAD_Status st, const char* what) {
        if (st == CAD_OK) { refresh(); return true; }
        say(QString("%1 실패: %2").arg(what, cadjson::lastError()));
        return false;
    }
    void say(const QString& m) { message_ = m; emit messageChanged(); }

    QVariantList kinds_, nodes_;
    QString summary_, message_;
    std::vector<uint32_t> objects_;
    double nextX_ = 0.0;
};
