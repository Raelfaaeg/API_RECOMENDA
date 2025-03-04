import pandas as pd
import json
import numpy as np
from fastapi import FastAPI
from scipy.spatial.distance import cdist  # Para calcular a distância
from sklearn.feature_extraction.text import TfidfVectorizer


app = FastAPI()

# Carregar os dados
contents = pd.read_csv("contents_clustered.csv")
interactions = pd.read_csv("interactions.csv")
teachers = pd.read_csv("teachers.csv")

# Converter features para formato numérico
contents["features"] = contents["features"].apply(lambda x: np.array(list(map(float, x.split(",")))))

# Criar dicionário para armazenar recomendações
recommendations_dict = {}

# Gerar recomendações para cada professor
for teacher_id, subject in zip(teachers["teacher_id"], teachers["subject"]):
    # Obter conteúdos usados pelo professor
    used_contents = interactions[interactions["teacher_id"] == teacher_id]["content_id"].tolist()

    if not used_contents:
        recommendations_dict[teacher_id] = {"message": "Nenhuma interação encontrada para este professor."}
        continue

    # Identificar cluster mais relevante com base nos conteúdos já usados
    clusters_used = contents[contents["content_id"].isin(used_contents)]["cluster"].value_counts()

    if clusters_used.empty:
        recommendations_dict[teacher_id] = {"message": "Nenhum cluster encontrado para este professor."}
        continue

    main_cluster = clusters_used.idxmax()

    # Filtrar conteúdos do mesmo cluster e da mesma disciplina do professor
    possible_recommendations = contents[
        (contents["cluster"] == main_cluster) &
        (~contents["content_id"].isin(used_contents)) &
        (contents["subject"] == subject)  # Filtra pela disciplina do professor
    ]

    if possible_recommendations.empty:
        recommendations_dict[teacher_id] = {"message": "Nenhum material relevante encontrado para recomendação."}
        continue

    # Obter features dos conteúdos já usados
    used_features = np.stack(contents[contents["content_id"].isin(used_contents)]["features"].values)

    # Obter features dos possíveis materiais recomendados
    possible_features = np.stack(possible_recommendations["features"].values)

    # Calcular distância entre cada material recomendado e os já usados
    distances = cdist(possible_features, used_features, metric="euclidean").mean(axis=1)

    # Ordenar os materiais pela menor distância (mais próximos primeiro)
    possible_recommendations = possible_recommendations.copy()
    possible_recommendations.loc[:, "distance"] = distances
    ordered_recommendations = possible_recommendations.sort_values(by="distance")["title"].tolist()

    # Selecionar os 5 primeiros
    recommendations_dict[teacher_id] = {"recommendations": ordered_recommendations[:5]}

# Salvar recomendações em um JSON
with open("recommendations.json", "w", encoding="utf-8") as f:
    json.dump(recommendations_dict, f, indent=4, ensure_ascii=False)





# Função para calcular a representação TF-IDF do arquivo recommendations.json
def generate_tfidf_from_recommendations():
    # Carregar o arquivo JSON com as recomendações
    with open("recommendations.json", "r", encoding="utf-8") as f:
        recommendations = json.load(f)

    # Extrair as recomendações para todos os professores
    recommendations_text = []
    for teacher_id, data in recommendations.items():
        if "recommendations" in data:
            # Concatenar as recomendações em um único texto para o professor
            recommendations_text.append(" ".join(data["recommendations"]))
        else:
            recommendations_text.append(data["message"])

    # Criar o vetor TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(recommendations_text)

    return tfidf_matrix, vectorizer

# Gerar a matriz TF-IDF
tfidf_matrix, vectorizer = generate_tfidf_from_recommendations()

# Exibir a matriz TF-IDF e as palavras associadas
print("Matriz TF-IDF:")
print(tfidf_matrix.toarray())  # Exibe a matriz de forma densa

# Exibir as palavras correspondentes aos índices da matriz TF-IDF
print("Palavras associadas aos índices:")
print(vectorizer.get_feature_names_out())