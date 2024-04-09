@echo off
chcp 65001 >nul 

:gremio
ipconfig 

set /p inf = "Testar conctividade, Digite a Informação: "

ping %inf%

set /p opcao="Deseja continuar? (S/N):"

if "%opcao%"=="S"(
    goto gremio
)