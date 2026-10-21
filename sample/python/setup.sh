#!/usr/bin/env bash
# LotCAD 파이썬 샘플 준비 (macOS · Ubuntu) — 가상환경(.venv)을 만들고 PySide6 를 설치한다.
# 시스템 패키지는 확인만 한다(설치엔 sudo 가 필요해 직접 하도록 명령을 알려 준다).
set -e
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"
if ! command -v "$PY" >/dev/null 2>&1; then
    echo "[오류] python3 가 필요합니다 (3.9 이상)."
    exit 1
fi
if ! "$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)'; then
    echo "[오류] 파이썬 3.9 이상이 필요합니다 — 지금: $("$PY" --version)"
    exit 1
fi

case "$(uname -s)" in
Darwin)
    LIB=libLotCADCore.dylib
    # 엔진 라이브러리는 Apple Silicon(arm64) 전용 — 파이썬도 arm64 여야 불러올 수 있다
    ARCH="$("$PY" -c 'import platform; print(platform.machine())')"
    if [ "$ARCH" != "arm64" ]; then
        echo "[경고] 이 파이썬은 $ARCH 입니다. 엔진은 arm64 전용 — Apple Silicon 용 파이썬(python.org 또는 Homebrew)을 쓰세요."
    fi
    ;;
Linux)
    LIB=libLotCADCore.so
    MISSING=""
    for so in libvulkan.so.1 libgtk-3.so.0 libX11.so.6 libxcb-cursor.so.0; do
        ldconfig -p 2>/dev/null | grep -q "$so" || MISSING="$MISSING $so"
    done
    if [ -n "$MISSING" ]; then
        echo "[경고] 없는 시스템 라이브러리:$MISSING"
        echo "  sudo apt install libvulkan1 mesa-vulkan-drivers libgtk-3-0 libxcb-cursor0"
    fi
    ;;
*)
    echo "[오류] macOS·Ubuntu 용 스크립트입니다. Windows 는 setup.bat."
    exit 1
    ;;
esac

if [ ! -f "../../sdk/$LIB" ]; then
    echo "[경고] sdk/$LIB 이 없습니다 — 엔진을 빌드하거나 Releases 에서 받아 sdk/ 에 넣으세요."
fi

if [ ! -x .venv/bin/python ]; then
    echo "가상환경 만드는 중 — .venv"
    if ! "$PY" -m venv .venv; then
        echo "[오류] 가상환경을 못 만들었습니다. Ubuntu: sudo apt install python3-venv"
        exit 1
    fi
fi
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt

echo
echo "준비 끝 — ./run.sh 로 실행하세요."
