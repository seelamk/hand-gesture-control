@echo off
REM Setup script for Hand Gesture Control System with Python 3.12
REM This script creates a virtual environment with Python 3.12 and installs dependencies

echo ========================================
echo Hand Gesture Control System Setup
echo ========================================
echo.

echo Step 1: Creating virtual environment with Python 3.12...
py -3.12 -m venv .venv312

if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    echo Make sure Python 3.12 is installed
    pause
    exit /b 1
)

echo SUCCESS: Virtual environment created
echo.

echo Step 2: Activating virtual environment...
call .venv312\Scripts\activate.bat

echo.
echo Step 3: Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Step 4: Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Please check the error messages above
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Installation complete
echo ========================================
echo.
echo Python version:
python --version
echo.
echo Installed packages:
pip list
echo.
echo ========================================
echo Next steps:
echo 1. Test camera: python test_camera.py
echo 2. Run application: python src/main.py
echo ========================================
echo.
echo To activate this environment in the future:
echo   .venv312\Scripts\activate
echo.
pause

