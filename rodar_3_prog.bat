@echo off
:: Ativar o ambiente Conda
call C:\ProgramData\Anaconda3\Scripts\activate.bat acoes_mod_ia

:: Navegar até o diretório do trabalho onde os scripts estão
cd C:\Users\rafae\Desktop\trabalho_ead

:: Executar o script criar_nomes.py
echo Executando criar_nomes.py...
python criar_nomes.py
if %errorlevel% neq 0 (
    echo Erro ao executar criar_nomes.py
    exit /b %errorlevel%
)

:: Executar o script treinar.py
echo Executando treinar.py...
python treinar.py
if %errorlevel% neq 0 (
    echo Erro ao executar treinar.py
    exit /b %errorlevel%
)

:: Executar o script escolher.py
echo Executando escolher.py...
python escolher.py
if %errorlevel% neq 0 (
    echo Erro ao executar escolher.py
    exit /b %errorlevel%
)

:: Exibir mensagem final
echo Todos os scripts foram executados com sucesso.
pause
