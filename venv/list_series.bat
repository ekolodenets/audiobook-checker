@echo off
chcp 65001 > nul
echo ===============================
echo   List All Series
echo ===============================

cd /d "C:\Users\ekolo\PycharmProjects\book_seeker"
python manage_series.py list

pause