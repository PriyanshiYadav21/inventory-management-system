@echo off

REM Setup script for local development on Windows

echo 🚀 Setting up Inventory Management System...

REM Backend setup
echo 📦 Setting up backend...
cd backend

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

echo ✅ Backend setup complete!

REM Frontend setup
echo 📦 Setting up frontend...
cd ..\frontend

REM Install dependencies
call npm install

echo ✅ Frontend setup complete!

echo.
echo 🎉 Setup complete! You can now start development:
echo.
echo Terminal 1 - Backend:
echo   cd backend
echo   venv\Scripts\activate
echo   python -m uvicorn app.main:app --reload
echo.
echo Terminal 2 - Frontend:
echo   cd frontend
echo   npm run dev
echo.
echo Then open http://localhost:5173 in your browser!

pause
