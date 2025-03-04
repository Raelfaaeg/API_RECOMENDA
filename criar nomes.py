import pandas as pd
import numpy as np
import random

# Criar professores
teachers = pd.DataFrame({
    "teacher_id": range(10),
    "name": [f"Professor {chr(65 + i)}" for i in range(10)],
    "subject": random.choices(["Matemática", "Português", "História"], k=10)
})
teachers.to_csv("teachers.csv", index=False)

# Criar conteúdos
contents = pd.DataFrame({
    "content_id": range(1000),
    "title": [f"Material {i}" for i in range(1000)],
    "subject": random.choices(["Matemática", "Português", "História"], k=1000),
    "features": [",".join(map(lambda x: f"{x:.3f}", np.random.rand(5))) for _ in range(1000)]
})
contents.to_csv("contents.csv", index=False)

# Criar interações
interactions = pd.DataFrame({
    "teacher_id": np.random.randint(0, 10, 30),
    "content_id": np.random.randint(0, 20, 30)
})
interactions.to_csv("interactions.csv", index=False)

print("CSVs gerados com sucesso!")
