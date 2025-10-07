@echo off
cls
echo.
echo ======================================================
echo           INICIANDO AUTOMATIZACION DE CORREO
echo ======================================================
echo.

REM Llama al interprete de Python para ejecutar el script
REM Nota: Reemplaza la ruta completa de Python si es diferente en tu sistema
"C:/Program Files/Python311/python.exe" email_sender.py

echo.
echo ======================================================
echo   PROCESO TERMINADO. Revisa las bandejas de correo.
echo ======================================================

pause