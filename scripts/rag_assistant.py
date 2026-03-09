import pandas as pd
import numpy as np
import faiss

from openai import OpenAI
from model_loader import get_model


# OpenAI client

client = OpenAI()


# Load documents

df = pd.read_csv("data/processed/documents_clean.csv")

embeddings = np.load("data/processed/embeddings.npy")


# Build FAISS index

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)


# Load embedding model

model = get_model()


# Ask user question

query = input("Ask a question about enterprise reports: ")


# Encode question

query_embedding = model.encode([query])


# Retrieve relevant reports

k = 5

distances, indices = index.search(query_embedding, k)


# Build context

context = ""

for i in range(k):

    idx = indices[0][i]

    context += df.iloc[idx]["document_text"] + "\n"


# Prompt for LLM

prompt = f"""
You are an enterprise analytics expert.

Use the reports below to answer the user's question.

Reports:
{context}

Question:
{query}

Explain clearly and mention patterns you observe.
"""


# Call OpenAI

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)


# Output answer

print("\nAI Insight:\n")

print(response.choices[0].message.content)