## Pré-requisitos

1. **Instalar o Anaconda** (caso não tenha):
   - Acesse [Anaconda](https://www.anaconda.com/products/individual) e faça o download do instalador.
   
2. **Instalar as dependências**:
   - Após instalar o Anaconda, crie e ative o ambiente virtual. Abra o terminal ou o Prompt de Comando e execute os seguintes comandos:

   ```bash
   conda create -n acoes_mod_ia python=3.9
   conda activate acoes_mod_ia

#Instalar as bibliotecas necessárias:

pip install fastapi uvicorn requests



Rode os programas na ordem:
"criar nomes.py"
"treinar.py"
"escolher.py"



#Abra o arquivo json ou rode "janela.py" para ver localmente

#ENavegue até o diretório onde o arquivo api.py está localizado

#Execute o servidor da API de recomendações com o comando abaixo. O servidor será iniciado na porta 8001:

uvicorn api:app --reload --host 0.0.0.0 --port 8001


#ENavegue até o diretório onde o arquivo intapi.py está localizado

#Execute o servidor da API de recomendações com o comando abaixo. O servidor será iniciado na porta 8002:

uvicorn intapi:app --reload --host 0.0.0.0 --port 8002


# Para acessar usando outra maquina na rede local use:
-No outro dispositivo, substitua 127.0.0.1 pelo IP da sua máquina:
-Para api.py (recomendações): http://192.168.1.5:8001/teachers ou http://192.168.1.5:8001/recommend/{teacher_id}
-Para intapi.py (interface interativa): http://192.168.1.5:8002/


alternativamente altere o caminho do ambiente e dos programas no arquivo rodar_3_prog.bat" "rodar_api.bat" e rode os programas nessa ordem.