#pragma once

// LayersApi — 도면층 · 선종류 · 블록 C API 브릿지(엔진 layer·linetype·블록 패널은 호스트 창에서 안 그려진다).
//
// 도면층: CAD_GetLayersJson(목록) · CAD_CreateLayer · CAD_RenameLayer · CAD_SetLayerVisible/Locked/Color/Linetype ·
//         CAD_AssignSelectedToLayer. (도면층 지우기·현재 도면층 API 는 아직 없다)
// 선종류: CAD_GetLinetypeIds · CAD_GetLinetypeName · CAD_SetObjectLinetype · CAD_SetLinetypeScale, .lin 불러오기는 명령 ltload.
// 블록:   CAD_GetBlocksJson · CAD_CreateBlock(기준점 = 선택 상자 바닥 중앙) · CAD_EntityExplode(삽입 한 단계 분해).
// 객체 수·선택 수는 밖(3D 뷰·명령)에서 바뀌므로 QML 이 패널을 보이는 동안 Timer 로 refresh() 한다.

#include "cad_json.h"

#include <QColor>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QObject>
#include <QString>
#include <QVariantList>
#include <QtQml/qqmlregistration.h>

#include <algorithm>
#include <vector>

class LayersApi : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    Q_PROPERTY(QVariantList layers    READ layers    NOTIFY changed)   // [{id,name,visible,locked,color:[r,g,b],linetypeId,objectCount,selectedCount}]
    Q_PROPERTY(QVariantList linetypes READ linetypes NOTIFY changed)   // [{id,name}] — 0 = Continuous
    Q_PROPERTY(QVariantList blocks    READ blocks    NOTIFY changed)   // [{name,objects,references,xref}]
    Q_PROPERTY(QString message READ message NOTIFY messageChanged)     // 마지막 결과·실패 이유

public:
    explicit LayersApi(QObject* parent = nullptr) : QObject(parent) {}

    QVariantList layers() const    { return layers_; }
    QVariantList linetypes() const { return linetypes_; }
    QVariantList blocks() const    { return blocks_; }
    QString message() const        { return message_; }

    Q_INVOKABLE void refresh() {
        const QVariantList layers = QJsonDocument::fromJson(cadjson::readBytes(&CAD_GetLayersJson)).object()
                                        .value("layers").toArray().toVariantList();
        const QVariantList blocks = QJsonDocument::fromJson(cadjson::readBytes(&CAD_GetBlocksJson)).object()
                                        .value("blocks").toArray().toVariantList();
        QVariantList lts;
        const int32_t n = CAD_GetLinetypeIds(nullptr, 0);
        std::vector<uint32_t> ids(size_t(std::max(n, 0)));
        if (n > 0) CAD_GetLinetypeIds(ids.data(), uint32_t(n));
        for (uint32_t id : ids) {
            char name[128] = {};
            CAD_GetLinetypeName(id, name, sizeof name);
            lts.append(QVariantMap{{"id", id}, {"name", QString::fromUtf8(name)}});
        }
        if (layers == layers_ && blocks == blocks_ && lts == linetypes_) return;
        layers_ = layers; blocks_ = blocks; linetypes_ = lts;
        emit changed();
    }

    // ── 도면층 ──
    Q_INVOKABLE int createLayer(const QString& name) {
        uint32_t id = 0;
        if (!check(CAD_CreateLayer(name.toUtf8().constData(), &id), "새 도면층")) return -1;   // 같은 이름 = CAD_E_DUPLICATE
        say(QString("도면층 '%1' 만듦").arg(name));
        return int(id);
    }
    Q_INVOKABLE void renameLayer(int id, const QString& name) { check(CAD_RenameLayer(uint32_t(id), name.toUtf8().constData()), "이름 바꾸기"); }
    Q_INVOKABLE void setVisible(int id, bool on) { check(CAD_SetLayerVisible(uint32_t(id), on), "보이기"); }
    Q_INVOKABLE void setLocked(int id, bool on)  { check(CAD_SetLayerLocked(uint32_t(id), on), "잠금"); }
    Q_INVOKABLE void setColor(int id, const QColor& c) {
        check(CAD_SetLayerColor(uint32_t(id), CAD_Color{c.redF(), c.greenF(), c.blueF()}), "색");
    }
    Q_INVOKABLE void setLayerLinetype(int id, int linetypeId) {
        check(CAD_SetLayerLinetype(uint32_t(id), uint32_t(linetypeId)), "도면층 선종류");
    }
    Q_INVOKABLE void assignSelected(int id, const QString& name) {
        uint32_t changed = 0;
        if (check(CAD_AssignSelectedToLayer(uint32_t(id), &changed), "도면층 옮기기"))
            say(changed ? QString("%1개를 도면층 '%2' 으로").arg(changed).arg(name) : "옮길 객체가 없습니다 — 3D 뷰에서 먼저 선택");
    }

    // ── 선종류 ──
    Q_INVOKABLE void applyLinetype(int linetypeId) {   // CAD_LINETYPE_BYLAYER(0xFFFFFFFF) = 도면층 따라
        const std::vector<uint32_t> ids = selection();
        if (ids.empty()) return say("선종류: 3D 뷰에서 객체를 먼저 선택하세요");
        uint32_t changed = 0;
        if (check(CAD_SetObjectLinetype(ids.data(), uint32_t(ids.size()), uint32_t(linetypeId), &changed), "선종류"))
            say(QString("선종류 — %1개").arg(changed));
    }
    Q_INVOKABLE void applyByLayer() { applyLinetype(int(CAD_LINETYPE_BYLAYER)); }
    Q_INVOKABLE void setLinetypeScale(double s) { if (check(CAD_SetLinetypeScale(s), "선종류 축척")) say(QString("LTSCALE %1").arg(s)); }
    Q_INVOKABLE void loadLinetypes() { CAD_CancelCommand(); CAD_ExecuteCommand("ltload"); }   // 명령행이 파일 이름을 묻는다

    // ── 블록 ──
    Q_INVOKABLE void createBlock(const QString& name) {
        const std::vector<uint32_t> ids = selection();
        if (ids.empty() || name.isEmpty()) return say("블록: 묶을 객체를 선택하고 이름을 넣으세요");
        uint32_t insertId = 0;
        if (check(CAD_CreateBlock(name.toUtf8().constData(), ids.data(), uint32_t(ids.size()), selectionBase(ids), &insertId), "블록 만들기"))
            say(QString("블록 '%1' — 객체 %2개, 삽입 #%3").arg(name).arg(ids.size()).arg(insertId));
    }
    Q_INVOKABLE void explodeSelected() {
        const std::vector<uint32_t> ids = selection();
        if (ids.empty()) return say("분해: 삽입(INSERT)을 먼저 선택하세요");
        const int32_t made = CAD_EntityExplode(ids.data(), uint32_t(ids.size()), false, nullptr, 0);   // 결과 id 는 필요 없으니 개수만
        say(made > 0 ? QString("분해: %1개가 됨").arg(made) : "분해 실패: " + cadjson::lastError());
    }

signals:
    void changed();
    void messageChanged();

private:
    bool check(CAD_Status st, const char* what) {
        refresh();
        if (st == CAD_OK) return true;
        say(QString("%1 실패: %2").arg(what, cadjson::lastError()));
        return false;
    }
    void say(const QString& m) { message_ = m; emit messageChanged(); }

    static std::vector<uint32_t> selection() {
        const int32_t n = CAD_GetSelection(nullptr, 0);
        std::vector<uint32_t> ids(size_t(n > 0 ? n : 0));
        if (n > 0) ids.resize(size_t(std::min<int32_t>(n, CAD_GetSelection(ids.data(), uint32_t(n)))));
        return ids;
    }
    // 기준점 = 선택 상자의 바닥 중앙(객체 JSON 의 bounds)
    static CAD_GeVec3 selectionBase(const std::vector<uint32_t>& ids) {
        double lo[3] = {1e30, 1e30, 1e30}, hi[3] = {-1e30, -1e30, -1e30};
        for (uint32_t id : ids) {
            const int32_t need = CAD_GetObjectJson(id, nullptr, 0);
            if (need <= 0) continue;
            QByteArray buf(need + 1, '\0');
            CAD_GetObjectJson(id, buf.data(), uint32_t(buf.size()));
            const QJsonObject b = QJsonDocument::fromJson(buf.left(int(qstrlen(buf.constData())))).object().value("bounds").toObject();
            const QJsonArray mn = b.value("min").toArray(), mx = b.value("max").toArray();
            for (int k = 0; k < 3 && mn.size() == 3; ++k) { lo[k] = std::min(lo[k], mn[k].toDouble()); hi[k] = std::max(hi[k], mx[k].toDouble()); }
        }
        if (lo[0] > hi[0]) return CAD_GeVec3{0, 0, 0};
        return CAD_GeVec3{(lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2, lo[2]};
    }

    QVariantList layers_, linetypes_, blocks_;
    QString message_;
};
