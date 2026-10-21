@echo off
rem LotCAD 파이썬 샘플 준비 (Windows) — 가상환경(.venv)을 만들고 PySide6 를 설치한다.
chcp 65001 >nul
setlocal
cd /d "%~dp0"

rem 파이썬 3.9 이상 — py 런처가 있으면 그것을, 없으면 PATH 의 python
set "PY=python"
where py >nul 2>nul && set "PY=py -3"
%PY% -c "import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)" 2>nul
if errorlevel 1 (
    echo [오류] 파이썬 3.9 이상이 필요합니다 — https://www.python.org/downloads/
    exit /b 1
)

if not exist "..\..\sdk\LotCADCore.dll" (
    echo [경고] sdk\LotCADCore.dll 이 없습니다 — 엔진을 빌드하거나 Releases 에서 받아 sdk\ 에 넣으세요.
)

if not exist ".venv\Scripts\python.exe" (
    echo 가상환경 만드는 중 — .venv
    %PY% -m venv .venv || exit /b 1
)
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt || exit /b 1

echo.
echo 준비 끝 — run.bat 으로 실행하세요.
