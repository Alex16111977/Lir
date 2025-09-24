@echo off
echo ========================================
echo    ADDING OUTPUT FOLDER TO REPOSITORY
echo ========================================
echo.

cd /d F:\AiKlientBank\Lir

echo [1] Checking current status...
git status --short output/ 2>nul | find /c /v "" > temp.txt
set /p count=<temp.txt
del temp.txt
echo    Files to add: %count%
echo.

echo [2] Adding output folder to git...
git add output/
echo    [OK] output/ added to staging
echo.

echo [3] Creating commit...
git commit -m "Add output folder with generated website

- Added complete generated website (55+ HTML files)
- A2 level lessons (15 lessons)
- B1 level lessons (15 lessons)  
- Thematic lessons (21 lessons)
- CSS/JS assets
- Main index.html"

echo.
echo [4] Status after commit:
git status --short
echo.

echo ========================================
echo    READY TO PUSH TO GITHUB
echo ========================================
echo.
echo Run: git push origin main
echo Or use GitHub Desktop to push changes
echo.
pause
