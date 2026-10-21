@echo off
rem LotCAD 파이썬 샘플 실행 (Windows) — setup.bat 을 먼저 한 번.
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    echo 먼저 setup.bat 을 실행하세요.
    exit /b 1
)
".venv\Scripts\python.exe" main.py %*
