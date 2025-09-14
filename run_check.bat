@echo off
chcp 65001 > nul
echo ===============================
echo   Audiobook Checker
echo ===============================
echo.

REM Активируем виртуальное окружение
call "C:\Users\ekolo\PycharmProjects\book_seeker\venv\Scripts\activate.bat"

REM Запускаем скрипт
python book_checker.py

echo.
pause