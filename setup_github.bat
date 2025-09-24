@echo off
echo ========================================
echo    LIR PROJECT - GITHUB SETUP
echo ========================================
echo.

echo [INFO] This script will help you create GitHub repository
echo [INFO] Make sure you have created a repository on GitHub first
echo.

echo [STEP 1] Current git status:
git status
echo.

echo [STEP 2] To connect to GitHub, run one of these commands:
echo.
echo Option A - HTTPS (recommended):
echo git remote add origin https://github.com/YOUR_USERNAME/Lir.git
echo git branch -M main
echo git push -u origin main
echo.
echo Option B - SSH (if you have SSH keys):
echo git remote add origin git@github.com:YOUR_USERNAME/Lir.git
echo git branch -M main  
echo git push -u origin main
echo.

echo [STEP 3] After connecting, you can use these commands:
echo git add .
echo git commit -m "Your commit message"
echo git push
echo.

echo [PROJECT INFO]
echo Repository name: Lir
echo Description: German Learning Platform through King Lear
echo Language: Python
echo License: MIT
echo.

pause
