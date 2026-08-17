# NexusLink Systems Unified Server Runner
Set-Location $PSScriptRoot

Write-Host "==============================================" -ForegroundColor Cyan
Write-Host " Starting NexusLink Server (FastAPI + Static) " -ForegroundColor Green
Write-Host " URL: http://localhost:8000/                 " -ForegroundColor Yellow
Write-Host "==============================================" -ForegroundColor Cyan

$pythonCmd = "python"
if (Test-Path "$PSScriptRoot\venv\Scripts\python.exe") {
    $pythonCmd = "$PSScriptRoot\venv\Scripts\python.exe"
}

& $pythonCmd "$PSScriptRoot\main.py"
