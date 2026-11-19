@echo off
title Seyes Editor
echo Starting Seyes Editor...
python "%~dp0main.py"
if %errorlevel% neq 0 (
    echo.
    echo An error occurred. Press any key to exit.
    pause >nul
)
