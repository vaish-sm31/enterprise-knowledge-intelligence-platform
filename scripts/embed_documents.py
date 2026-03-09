import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

df = pd.read_csv("data/raw/documents.csv")

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = df["document_text"].tolist()

embeddings = model.encode(texts)

np.save("data/processed/embeddings.npy", embeddings)

df.to_csv("data/processed/documents_clean.csv", index=False)