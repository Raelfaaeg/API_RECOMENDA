import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def index():
    """Página principal que mostra a lista de teachers"""
    try:
        # Fazendo uma requisição GET para a API da recomendação
        response = requests.get("http://127.0.0.1:8001/teachers")
        teacher_data = response.json()
        
        if "teacher_ids" in teacher_data:
            teacher_ids = teacher_data["teacher_ids"]
            # Gerando uma lista de links para cada teacher_id
            html_content = "<h1>Lista de Professores</h1><ul>"
            for teacher_id in teacher_ids:
                html_content += f'<li><a href="/recommend/{teacher_id}">Professor {teacher_id}</a></li>'
            html_content += "</ul>"
            return HTMLResponse(content=html_content)
        else:
            return HTMLResponse(content="<h1>Erro ao carregar os professores</h1>")

    except Exception as e:
        return HTMLResponse(content=f"<h1>Erro: {str(e)}</h1>")

@app.get("/recommend/{teacher_id}")
def recommend(teacher_id: int):
    """Retorna as recomendações do professor a partir da API"""
    try:
        # Fazendo uma requisição GET para a API da recomendação
        response = requests.get(f"http://127.0.0.1:8001/recommend/{teacher_id}")
        recommendation_data = response.json()

        if "recommendations" in recommendation_data:
            recommendations = recommendation_data["recommendations"]
            html_content = f"<h1>Recomendações para o Professor {teacher_id}</h1><ul>"
            for rec in recommendations:
                html_content += f"<li>{rec}</li>"
            html_content += "</ul>"
            return HTMLResponse(content=html_content)
        else:
            return HTMLResponse(content="<h1>Professor não encontrado</h1>")
        
    except Exception as e:
        return HTMLResponse(content=f"<h1>Erro: {str(e)}</h1>")
