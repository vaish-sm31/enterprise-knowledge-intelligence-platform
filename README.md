# Enterprise Knowledge Intelligence Platform

![Dashboard Preview](screenshots/dashboard_overview.png)

AI system for detecting duplicated analytical work, enabling semantic discovery of enterprise reports, and estimating operational knowledge waste.

Large organizations generate thousands of internal reports across departments. Because teams often work in silos, analysts frequently recreate analyses that already exist elsewhere in the company.

This project demonstrates how semantic embeddings, vector similarity search, and retrieval-augmented generation (RAG) can be used to identify duplicated analytical work and improve knowledge reuse.

---

# Problem

In many organizations:

- Analysts independently create reports on similar topics
- Knowledge becomes fragmented across teams
- Analysts recreate analyses because previous work is difficult to locate

Most internal knowledge systems rely on keyword search, which fails when similar analyses are described using different terminology.

Organizations therefore struggle to discover and reuse existing analytical knowledge.

---

# Solution

This project simulates an enterprise analytics environment and builds a pipeline that:

- Converts reports into semantic embeddings
- Detects structurally similar reports using vector similarity search
- Estimates duplicated analytical effort
- Enables semantic discovery of enterprise reports
- Provides AI-assisted explanations of knowledge patterns

The result is a prototype Knowledge Intelligence Platform that surfaces duplicated work and improves analytical knowledge reuse.

---

# Business Case

Enterprise Knowledge Intelligence Platform – Business Case

Business Case Document: docs/business_case_enterprise_knowledge_platform.pdf

The document outlines:

- operational inefficiencies caused by duplicated analytics reports
- how semantic search improves knowledge reuse
- estimated cost impact of duplicated analytical work
- recommendations for enterprise knowledge management systems

This analysis presents the project from a business decision-making perspective, similar to how data teams communicate insights to leadership.

---

# System Architecture

![System Architecture](screenshots/architecture.png)

Pipeline Overview

Synthetic Enterprise Reports  
↓  
Sentence Transformer Embeddings  
↓  
FAISS Vector Similarity Search  
↓  
Duplicate Report Detection  
↓  
Knowledge ROI Analysis  
↓  
Streamlit Intelligence Dashboard

---

# Methodology

## Synthetic Enterprise Data

Enterprise reports cannot be publicly shared, so this project generates synthetic enterprise reports using structured templates representing common analytical topics across departments.

The simulation dataset contains 200 synthetic enterprise reports distributed across multiple departments and analytical themes. Documents discussing similar analytical topics intentionally contain overlapping language patterns to simulate real enterprise knowledge duplication.

---

## Semantic Embeddings

Reports are converted into semantic vectors using Sentence Transformers (MiniLM).

Unlike keyword-based approaches, transformer embeddings capture the semantic meaning of text, allowing the system to identify reports describing similar analytical work even when wording differs.

---

## Vector Similarity Search

Embeddings are indexed using FAISS, enabling efficient nearest-neighbor search across document vectors.

This allows the system to discover semantically related reports even when titles or keywords differ.

---

## Duplicate Detection

Reports are compared using vector similarity distance.

Lower distance values indicate stronger semantic similarity between documents.

Pairs with similarity distance below 0.35 were classified as potential duplicates after manual inspection of similarity distributions.

---

## Validation

A manually labeled validation sample was used to evaluate duplicate detection performance.

Precision: 1.00  
Recall: 0.92  
F1 Score: 0.96  

These results indicate strong performance in identifying semantically similar analytical reports.

---

# Dashboard

## Executive Overview

![Dashboard Overview](screenshots/dashboard_overview.png)

Displays:

- total reports analyzed
- duplicate report percentage
- estimated analyst effort wasted
- department-level duplication patterns

Example dashboard metrics from the simulation:

Total Reports: 200  
Duplicate Reports: 168  
Duplicate Rate: 84%  
Estimated Cost Waste: $78,240

---

## Duplicate Report Detection

![Duplicate Reports](screenshots/duplicate_detection.png)

Identifies reports with highly similar analytical structure using semantic similarity analysis.

---

## Semantic Knowledge Search

![Semantic Search](screenshots/semantic_search.png)

Users can search enterprise reports using natural language queries rather than exact report titles.

---

## AI Knowledge Assistant

![RAG Assistant](screenshots/rag_assistant.png)

Retrieves relevant reports and generates explanations about analytical patterns and duplicated work.

---

# KPI Framework for Knowledge Reuse

Organizations implementing knowledge intelligence systems need measurable indicators of knowledge reuse.

| KPI | Definition | Purpose |
|----|----|----|
| Duplicate Report Rate | Percentage of reports identified as structurally similar | Measures duplicated analytical work |
| Knowledge Reuse Rate | Percentage of analyses referencing previous reports | Measures knowledge reuse |
| Search Success Rate | Percentage of queries returning relevant reports | Evaluates discovery effectiveness |
| Analyst Hours Saved | Estimated analyst time saved through reuse | Measures productivity gains |
| Cost Avoidance | Estimated operational cost prevented | Quantifies financial impact |

These metrics help organizations move toward data-driven knowledge management systems.

---

# Technologies Used

- Python
- Sentence Transformers (MiniLM)
- FAISS Vector Search
- Streamlit
- Pandas
- NumPy
- scikit-learn (evaluation metrics)
- OpenAI API

---

# Project Structure

enterprise-knowledge-intelligence-platform

app/  
dashboard.py  

scripts/  
generate_data.py  
embed_documents.py  
detect_duplicates.py  
evaluate_duplicates.py  
knowledge_search.py  
rag_assistant.py  
recommend_actions.py  
calculate_roi.py  

data/  
raw/  
processed/  

screenshots/  

README.md  
requirements.txt

---

# Pipeline

1. Generate synthetic enterprise reports  
python scripts/generate_data.py

2. Create semantic embeddings  
python scripts/embed_documents.py

3. Detect semantically similar reports  
python scripts/detect_duplicates.py

4. Evaluate duplicate detection  
python scripts/evaluate_duplicates.py

5. Estimate duplicated analytical effort  
python scripts/calculate_roi.py

6. Run semantic knowledge search  
python scripts/knowledge_search.py

7. Generate AI explanations (RAG)  
python scripts/rag_assistant.py

8. Launch dashboard  
streamlit run app/dashboard.py

---

# Key Concepts Demonstrated

- Semantic document embeddings
- Vector similarity search
- Duplicate knowledge detection
- Retrieval-augmented generation (RAG)
- Knowledge reuse analytics
- AI-assisted business intelligence dashboards
