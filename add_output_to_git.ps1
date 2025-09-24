# PowerShell скрипт для добавления output в Git

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   ADDING OUTPUT TO GITHUB REPOSITORY" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Set-Location -Path "F:\AiKlientBank\Lir"

# Проверка статуса
Write-Host "[1] Current git status:" -ForegroundColor Yellow
git status --short | Select-String "output/"
Write-Host ""

# Добавление output
Write-Host "[2] Adding output folder..." -ForegroundColor Yellow
git add output/
Write-Host "    [OK] Added to staging area" -ForegroundColor Green
Write-Host ""

# Коммит
Write-Host "[3] Creating commit..." -ForegroundColor Yellow
git commit -m "Add output folder with generated website`n`n- Complete German learning website`n- 55+ HTML pages`n- All lessons (A2, B1, Thematic)`n- CSS/JS assets`n- Ready for deployment"
Write-Host ""

# Push
Write-Host "[4] Pushing to GitHub..." -ForegroundColor Yellow
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "   SUCCESS! OUTPUT FOLDER ADDED TO GITHUB" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "View at: https://github.com/Alex16111977/Lir" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "[ERROR] Push failed. Try manual push in GitHub Desktop" -ForegroundColor Red
}

Write-Host ""
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
