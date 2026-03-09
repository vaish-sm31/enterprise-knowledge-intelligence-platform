import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import pandas as pd
import numpy as np
import faiss

from openai import OpenAI
from scripts.model_loader import get_model


st.set_page_config(page_title="Knowledge ROI Dashboard", layout="wide")

st.title("Enterprise Knowledge Intelligence Platform")


# Load data

roi = pd.read_csv("data/processed/roi_summary.csv")
actions = pd.read_csv("data/processed/action_recommendations.csv")
duplicates = pd.read_csv("data/processed/duplicate_reports.csv")
documents = pd.read_csv("data/processed/documents_clean.csv")

embeddings = np.load("data/processed/embeddings.npy")


# Metrics

total_reports = roi["total_reports"][0]
duplicate_reports = roi["duplicate_reports"][0]
duplicate_percentage = roi["duplicate_percentage"][0]
duplicate_cost = roi["estimated_duplicate_cost"][0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Reports", total_reports)
col2.metric("Duplicate Reports", duplicate_reports)
col3.metric("Duplicate %", f"{duplicate_percentage:.2%}")
col4.metric("Estimated Cost Waste", f"${duplicate_cost:,.0f}")


# Department Breakdown

st.subheader("Department Duplication Breakdown")

dept_counts = actions["department"].value_counts()

st.bar_chart(dept_counts)


# Duplicate Reports Table

st.subheader("Duplicate Report Pairs")

st.dataframe(
    duplicates[[
        "doc_a_title",
        "doc_b_title",
        "distance"
    ]].head(50)
)


# Recommended Actions

st.subheader("Recommended Actions")

st.dataframe(
    actions[[
        "doc_id",
        "title",
        "department",
        "creation_cost",
        "views",
        "recommended_action"
    ]]
)


# Build vector index

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

model = get_model()


# Semantic Search

st.subheader("Semantic Report Search")

search_query = st.text_input("Search enterprise reports")

if search_query:

    query_embedding = model.encode([search_query])

    distances, indices = index.search(query_embedding, 5)

    results = []

    for i in range(5):

        idx = indices[0][i]

        results.append({
            "title": documents.iloc[idx]["title"],
            "department": documents.iloc[idx]["department"],
            "views": documents.iloc[idx]["views"]
        })

    st.dataframe(pd.DataFrame(results))


# RAG Assistant

st.subheader("AI Knowledge Assistant")

question = st.text_input("Ask AI about report patterns")

if question:

    client = OpenAI()

    query_embedding = model.encode([question])

    distances, indices = index.search(query_embedding, 5)

    context = ""

    for i in range(5):

        idx = indices[0][i]

        context += documents.iloc[idx]["document_text"] + "\n"

    prompt = f"""
You are an enterprise analytics expert.

Use the reports below to answer the user's question.

Reports:
{context}

Question:
{question}

Explain clearly and mention patterns you observe.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)