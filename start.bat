@echo off
setlocal

echo Checking for virtual environment...
if not exist venv (
    echo Virtual environment not found. Creating one...
    python -m venv venv

    if errorlevel 1 (
        echo Failed to create virtual environment!
        pause
        exit /b
    )

    echo Installing dependencies from requirements.txt...
    call venv\Scripts\activate && pip install -r requirements.txt
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Applying migrations...
python manage.py migrate

echo Starting Django with development server...
python manage.py runserver

:: Keep window open to view errors
pause
