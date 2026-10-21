#!/usr/bin/env bash
# LotCAD 파이썬 샘플 실행 (macOS · Ubuntu) — ./setup.sh 를 먼저 한 번.
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
    echo "먼저 ./setup.sh 를 실행하세요."
    exit 1
fi
exec .venv/bin/python main.py "$@"
