@echo off
chcp 65001 > nul
:menu
cls
echo ===============================
echo   AUDIOBOOK CHECKER MENU
echo ===============================
echo.
echo 1. Check for updates
echo 2. Add new series
echo 3. List all series
echo 4. Remove series
echo 5. Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" goto check
if "%choice%"=="2" goto add
if "%choice%"=="3" goto list
if "%choice%"=="4" goto remove
if "%choice%"=="5" exit

echo Invalid choice! Press any key to try again.
pause > nul
goto menu

:check
call "C:\Users\ekolo\PycharmProjects\book_seeker\venv\Scripts\activate.bat"
python book_checker.py
pause
goto menu

:add
cd /d "C:\Users\ekolo\PycharmProjects\book_seeker"
python manage_series.py add
pause
goto menu

:list
cd /d "C:\Users\ekolo\PycharmProjects\book_seeker"
python manage_series.py list
pause
goto menu

:remove
cd /d "C:\Users\ekolo\PycharmProjects\book_seeker"
python manage_series.py remove
pause
goto menu