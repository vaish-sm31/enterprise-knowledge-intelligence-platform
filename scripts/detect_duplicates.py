import pandas as pd
import numpy as np
import faiss

df = pd.read_csv("data/processed/documents_clean.csv")

embeddings = np.load("data/processed/embeddings.npy")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

k = 5

distances, indices = index.search(embeddings, k)

results = []

for i in range(len(indices)):
    for j in range(1, k):

        neighbor_index = indices[i][j]

        if neighbor_index == i:
            continue

        distance = distances[i][j]

        if distance < 0.6:

            results.append({
                "doc_a_id": df.iloc[i]["doc_id"],
                "doc_a_title": df.iloc[i]["title"],
                "doc_b_id": df.iloc[neighbor_index]["doc_id"],
                "doc_b_title": df.iloc[neighbor_index]["title"],
                "distance": distance
            })

duplicates = pd.DataFrame(results)

duplicates.to_csv("data/processed/duplicate_reports.csv", index=False)