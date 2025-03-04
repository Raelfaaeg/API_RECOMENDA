from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/teachers")
def get_teachers():
    """Retorna todos os teacher_ids disponíveis no JSON gerado."""
    try:
        print("Acessando a rota /teachers")  # Print para ver se a rota está sendo chamada
        with open("recommendations.json", "r", encoding="utf-8") as f:
            recommendations = json.load(f)
        
        teacher_ids = list(recommendations.keys())
        print(f"teacher_ids encontrados: {teacher_ids}")  # Verificação se os dados estão sendo carregados corretamente
        return {"teacher_ids": teacher_ids}
    except Exception as e:
        print(f"Erro ao acessar /teachers: {str(e)}")  # Print de erro
        return {"error": str(e)}

@app.get("/recommend/{teacher_id}")
def recommend(teacher_id: int):
    """Retorna as recomendações do professor a partir do JSON gerado."""
    try:
        print(f"Acessando a rota /recommend/{teacher_id}")  # Print para ver se a rota está sendo chamada corretamente
        with open("recommendations.json", "r", encoding="utf-8") as f:
            recommendations = json.load(f)
        
        result = recommendations.get(str(teacher_id), {"message": "Professor não encontrado."})
        print(f"Resultado para {teacher_id}: {result}")  # Verificação se o professor existe no arquivo
        return result
    except Exception as e:
        print(f"Erro ao acessar /recommend/{teacher_id}: {str(e)}")  # Print de erro
        return {"error": str(e)}
