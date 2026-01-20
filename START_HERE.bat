@echo off
title Credit Card Detection Server
color 0A
echo ========================================
echo   Credit Card Detection System
echo ========================================
echo.
echo Starting server...
echo.
echo Open your browser and visit:
echo http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.
cd /d "%~dp0"
py api.py
pause
