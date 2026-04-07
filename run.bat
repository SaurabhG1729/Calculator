@echo off
cls
echo [LAUNCHING] C-Powered Calculator...

:: Change the directory to the location of this script
cd /d "%~dp0"


".\venv\Scripts\python.exe" main_connector.py

:: 3. Only show error if the python script actually crashes
if errorlevel 1 (
    echo.
    echo [ERROR] Application failed. Check if PyQt6 is installed in the venv.
    pause
)