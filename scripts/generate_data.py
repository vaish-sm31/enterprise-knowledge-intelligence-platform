import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

departments = [
    "Finance",
    "Marketing",
    "Sales",
    "Product",
    "Operations",
    "Customer Success",
    "Strategy"
]

topics = [
    "customer segmentation",
    "revenue forecast",
    "campaign performance",
    "customer churn",
    "product adoption",
    "sales pipeline",
    "market expansion",
    "pricing strategy",
    "user retention"
]

documents = []

n_docs = 300

for i in range(n_docs):

    dept = random.choice(departments)
    topic = random.choice(topics)

    title = f"{topic.title()} Analysis"

    creation_hours = random.choice([4,6,8,10,12])

    base_text = f"""
    This report analyzes {topic} trends across the {dept} department.
    The analysis focuses on key drivers, historical performance,
    and projected outcomes for the next quarter.
    """

    documents.append({
        "doc_id": i,
        "title": title,
        "department": dept,
        "author": fake.name(),
        "creation_hours": creation_hours,
        "document_text": base_text,
        "created_date": fake.date_between(start_date="-2y", end_date="today"),
        "views": np.random.pareto(2) * 50
    })

df = pd.DataFrame(documents)

df["views"] = df["views"].astype(int)

df.to_csv("data/raw/documents.csv", index=False)