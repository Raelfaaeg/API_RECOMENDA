@echo off
:: Ativar o ambiente Conda
call C:\ProgramData\Anaconda3\Scripts\activate.bat acoes_mod_ia

:: Navegar até o diretório do trabalho
cd C:\Users\rafae\Desktop\trabalho_ead

:: Iniciar o servidor FastAPI para as recomendações (api.py)
start uvicorn api:app --reload --host 0.0.0.0 --port 8001

:: Esperar um momento para garantir que o servidor foi iniciado
timeout /t 5

:: Iniciar o servidor FastAPI para a interface interativa (intapi.py)
start uvicorn intapi:app --reload --host 0.0.0.0 --port 8002

:: Abrir o navegador automaticamente na interface interativa
start http://127.0.0.1:8002
