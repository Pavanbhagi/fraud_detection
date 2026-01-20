Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Credit Card Detection System" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting server..." -ForegroundColor Green
Write-Host ""
Write-Host "Open your browser and visit:" -ForegroundColor Yellow
Write-Host "http://localhost:8000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

Set-Location $PSScriptRoot
py api.py
