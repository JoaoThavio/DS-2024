@echo off 
chcp 65001 >nul

:gremio
echo Escolha uma Opção
echo 1 - Calculadora
echo 2 - Bloco de Notas
echo 3 - Paint

set /p opcao="Digite sua Opção: "

if "%opcao%"=="1" (
    start calc.exe
)
if "%opcao%"=="2" (
    start notepad.exe
)
if "%opcao%"=="3" (
    start mspaint.exe
)
cls
goto gremio