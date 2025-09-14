@echo off
chcp 65001 > nul
echo ===============================
echo   Remove Series
echo ===============================

cd /d "C:\Users\ekolo\PycharmProjects\book_seeker"
python manage_series.py remove

pause