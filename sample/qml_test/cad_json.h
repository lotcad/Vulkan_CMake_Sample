#pragma once

// 엔진의 "JSON 문자열을 돌려주는" C API 를 Qt 자료형으로 읽는 공용 헬퍼.
//
// 엔진 규약(2회 호출): out=NULL/cap=0 으로 먼저 불러 **필요한 길이**를 받고,
// 그만큼 버퍼를 잡아 다시 부른다. 길이를 모른 채 고정 버퍼로 부르면 긴 결과가 잘린다
// (도면 뷰 목록은 뷰마다 치수·출처가 붙어 금방 수 KB 가 된다).

#include "../../sdk/include/LotCAD_API.h"

#include <QByteArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QString>
#include <QVariantList>

namespace cadjson {

// fn(char* out, 칸) 꼴 API 를 읽어 바이트열로. 실패/빈 결과면 빈 QByteArray.
// 칸 형은 함수마다 다르다(새 규칙 uint32_t · 옛 함수 int) — 템플릿으로 둘 다 받는다.
template <class R, class Cap>
QByteArray readBytes(R (*fn)(char*, Cap)) {
    const int need = int(fn(nullptr, Cap(0)));
    if (need > 0) {
        QByteArray buf(need + 1, '\0');          // +1 = 널 종료 여유
        const int n = int(fn(buf.data(), Cap(buf.size())));
        if (n <= 0) return {};
        buf.resize(qMin(n, int(buf.size())));
        return buf;
    }
    // 길이 질의를 지원하지 않는(0 을 주는) 함수가 섞여 있어도 쓸 수 있게 한 번 더 시도한다.
    QByteArray buf(64 * 1024, '\0');
    const int n = int(fn(buf.data(), Cap(buf.size())));
    if (n <= 0) return {};
    buf.resize(qMin(n, int(buf.size())));
    return buf;
}

template <class R, class Cap>
QJsonObject readObject(R (*fn)(char*, Cap)) {
    return QJsonDocument::fromJson(readBytes(fn)).object();
}

// 배열 JSON → QML model 로 바로 쓸 수 있는 QVariantList (원소는 QVariantMap).
template <class R, class Cap>
QVariantList readArray(R (*fn)(char*, Cap)) {
    return QJsonDocument::fromJson(readBytes(fn)).array().toVariantList();
}

// 실패 사유 — 0/false 를 돌려준 API 직후에 읽는다.
inline QString lastError() {
    char buf[1024] = {0};
    const int32_t n = CAD_GetLastError(buf, uint32_t(sizeof(buf)));
    return n > 0 ? QString::fromUtf8(buf, n) : QString();
}

}   // namespace cadjson
