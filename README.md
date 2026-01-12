# 🚀 Enterprise RAG-LLMOps Pipeline

An end-to-end **LLMOps (Large Language Model Operations)** framework designed for building, evaluating, and maintaining production-ready **RAG (Retrieval-Augmented Generation)** systems. This project focuses on reliability, security, and automated quality governance.

## 🌟 Overview

In modern AI applications, especially for government (SAM.gov) and enterprise sectors, "hallucination" and "outdated information" are critical risks. This project demonstrates a robust pipeline that ensures:
1. **Continuous Integration (CI)** for RAG components.
2. **Continuous Evaluation (CE)** of answer quality using the Ragas framework.
3. **Automated Ingestion** to keep the knowledge base updated.

## 🛠 Tech Stack

* **Orchestration**: LangChain
* **LLM**: OpenAI GPT-4o / Claude 3.5
* **Vector Database**: ChromaDB (Open-source, self-hostable)
* **Evaluation**: Ragas (Retrieval-Augmented Generation Assessment)
* **Ops/CI-CD**: GitHub Actions
* **Data Management**: DVC (Data Version Control)

## 📁 Project Structure

```text
├── .github/workflows/       # CI/CD & Automated Evaluation Pipelines
│   └── eval_rag.yml         # Runs RAGAS metrics on every push
├── data/                    # Source documents (PDF, Markdown, etc.)
├── src/
│   ├── ingest.py            # Document parsing and Vector DB embedding
│   ├── retrieve.py          # Semantic search logic
│   └── chain.py             # LLM RAG chain implementation
├── tests/
│   └── test_eval.py         # Automated QA tests (Faithfulness, Relevance)
└── requirements.txt         # Dependency management
