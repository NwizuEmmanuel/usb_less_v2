@echo off
REM filepath: .\StartApp.bat

REM Check for Python
where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed or not added to PATH.
    echo Please download and install Python from https://www.python.org/downloads/
    pause
    exit /b
)

REM Check for Tkinter
python -c "import tkinter" 2>nul
if errorlevel 1 (
    echo Tkinter is not installed.
    echo Please install Tkinter. On Windows, it is usually included with Python.
    echo If you installed Python without Tkinter, run:
    echo     python -m pip install tk
    pause
    exit /b
)

REM Run the application
python app.py
pause