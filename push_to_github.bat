@echo off
echo ========================================
echo    PUSHING LIR PROJECT TO GITHUB
echo ========================================
echo.

echo [INFO] Repository: https://github.com/Alex16111977/Lir
echo.

echo [STEP 1] Current status:
git status --short
echo.

echo [STEP 2] Current branch:
git branch
echo.

echo [STEP 3] Remote configuration:
git remote -v
echo.

echo [STEP 4] Pushing to GitHub...
echo.
git push -u origin main

echo.
echo ========================================
echo    OPERATION COMPLETE
echo ========================================
echo.
echo If successful, your project is now on GitHub!
echo URL: https://github.com/Alex16111977/Lir
echo.
pause
