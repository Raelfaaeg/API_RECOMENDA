import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Carregar dados
contents = pd.read_csv("contents.csv")

# Converter features para matriz numérica
features = np.array([list(map(float, row.split(","))) for row in contents["features"]])

# Treinar modelo K-Means (número de clusters arbitrário)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
contents["cluster"] = kmeans.fit_predict(features)

# Salvar resultados
contents.to_csv("contents_clustered.csv", index=False)

print("Modelo treinado e clusters salvos!")
