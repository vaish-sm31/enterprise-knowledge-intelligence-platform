import pandas as pd
import numpy as np
import faiss

from model_loader import get_model


# Load documents

df = pd.read_csv("data/processed/documents_clean.csv")

embeddings = np.load("data/processed/embeddings.npy")


# Build FAISS index

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)


# Load embedding model

model = get_model()


# Ask user query

query = input("Ask about existing reports: ")


# Encode query


query_embedding = model.encode([query])



# Search similar reports

k = 5

distances, indices = index.search(query_embedding, k)


# Display results

print("\nMost relevant reports:\n")


for i in range(k):

    idx = indices[0][i]

    title = df.iloc[idx]["title"]

    department = df.iloc[idx]["department"]

    views = df.iloc[idx]["views"]

    print(
        f"{title} - {department} (views: {views})"
    )