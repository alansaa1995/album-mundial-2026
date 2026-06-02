@echo off
title Cerrando Album Mundial 2026...
echo Cerrando el servidor...
taskkill /F /IM uvicorn.exe >nul 2>&1
taskkill /F /IM python.exe /FI "WINDOWTITLE eq Album*" >nul 2>&1

:: Matar por puerto 8000 por las dudas
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8000"') do (
    taskkill /F /PID %%a >nul 2>&1
)

echo Servidor detenido.
timeout /t 2 /nobreak >nul
