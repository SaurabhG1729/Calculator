@echo off
setlocal
echo ========================================
echo   C-ENGINE CALCULATOR BUILD SYSTEM
echo ========================================

if not exist "build" mkdir build

echo Choose Build Type:
echo [1] Release (Optimized, No Debug)
echo [2] Debug   (Includes -g for GDB)
set /p choice="Enter choice (1-2): "

if "%choice%"=="1" (
    echo Building RELEASE version...
    gcc -O3 -shared -o build/main.dll main.c
) else if "%choice%"=="2" (
    echo Building DEBUG version...
    gcc -g -shared -o build/main.dll main.c
) else (
    echo Invalid choice. Exiting.
    exit /b 1
)

if %errorlevel% neq 0 (
    echo [ERROR] Compilation failed!
    pause
    exit /b %errorlevel%
)

echo [SUCCESS] DLL generated in /build folder.
pause