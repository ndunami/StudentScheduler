@echo off
setlocal

echo Checking for virtual environment...
if not exist venv (
    echo Virtual environment not found. Creating one...
    py -m venv venv

    if errorlevel 1 (
        echo Failed to create virtual environment!
        pause
        exit /b
    )

    echo Activating virtual environment...
    call venv\Scripts\activate

    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt || (echo Failed to install dependencies! & pause & exit /b)
) else (
    echo Virtual environment found.
    call venv\Scripts\activate
)

:: Apply migrations only if necessary
py manage.py migrate --check > nul
if %errorlevel% neq 0 (
    echo Applying migrations...
    py manage.py migrate
) else (
    echo No migrations needed.
)

echo Starting Django development server...
py manage.py runserver

:: Keep window open
pause
