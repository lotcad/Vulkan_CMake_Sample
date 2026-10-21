#!/usr/bin/env bash
# LotCAD 파이썬 샘플 준비 (macOS · Ubuntu) — 가상환경(.venv)을 만들고 PySide6 를 설치한다.
# Ubuntu 는 없는 시스템 패키지를 모아 물어보고 sudo apt-get 으로 설치한다(-y 면 묻지 않고, 터미널이 아니면 명령만 알려 준다).
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
    # 없는 것을 모두 모아 apt 명령 하나로 — 하나 깔고 다시 돌리면 다음 것이 나오는 일이 없게
    PKGS=""
    if ! "$PY" -c 'import ensurepip' >/dev/null 2>&1; then
        PKGS="$PKGS python$("$PY" -c 'import sys; print("%d.%d" % sys.version_info[:2])')-venv"
    fi
    for pair in libvulkan.so.1:libvulkan1 libgtk-3.so.0:libgtk-3-0 libX11.so.6:libx11-6 libxcb-cursor.so.0:libxcb-cursor0; do
        ldconfig -p 2>/dev/null | grep -q "${pair%%:*}" || PKGS="$PKGS ${pair#*:}"
    done
    # Vulkan 드라이버(ICD) — NVIDIA 독점 드라이버는 자기 ICD 를 깔아 두니 아무것도 없을 때만 mesa
    if ! compgen -G '/usr/share/vulkan/icd.d/*.json' >/dev/null && ! compgen -G '/etc/vulkan/icd.d/*.json' >/dev/null; then
        PKGS="$PKGS mesa-vulkan-drivers"
    fi
    if [ -n "$PKGS" ]; then
        echo "필요한 시스템 패키지가 없습니다:$PKGS"
        if ! command -v apt-get >/dev/null 2>&1; then
            echo "[오류] apt 가 없는 배포판입니다 — 위 패키지에 해당하는 것을 직접 설치한 뒤 다시 실행하세요."
            exit 1
        fi
        ANSWER=""
        if [ "$1" = "-y" ]; then
            ANSWER=y
        elif [ -t 0 ]; then
            read -r -p "지금 설치할까요? (sudo apt-get install) [Y/n] " ANSWER
            ANSWER="${ANSWER:-y}"
        fi
        case "$ANSWER" in
        [Yy]*) sudo apt-get install -y $PKGS ;;
        *)
            echo "직접 설치한 뒤 다시 실행하세요:"
            echo "  sudo apt install$PKGS"
            exit 1
            ;;
        esac
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

# pip 까지 확인 — Ubuntu 에서 python3-venv 없이 venv 가 실패하면 pip 없는 .venv/bin/python 만 남는다
if ! .venv/bin/python -m pip --version >/dev/null 2>&1; then
    rm -rf .venv
    echo "가상환경 만드는 중 — .venv"
    if ! "$PY" -m venv .venv; then
        rm -rf .venv
        echo "[오류] 가상환경을 못 만들었습니다. Ubuntu: sudo apt install python3-venv"
        exit 1
    fi
fi
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt

echo
echo "준비 끝 — ./run.sh 로 실행하세요."
