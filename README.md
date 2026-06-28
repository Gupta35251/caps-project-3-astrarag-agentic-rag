# caps-project-3-astrarag-agentic-rag

# 🌱 AstraRAG - Agentic RAG Question Answering System

An Agentic Retrieval-Augmented Generation (RAG) application that answers user questions from uploaded documents using **CrewAI**, **LangChain**, **ChromaDB**, **Groq LLM**, **FastAPI**, and **Streamlit**.

---

## 🚀 Features

- 📄 Document ingestion from PDF files
- 🔍 Semantic search using Chroma Vector Database
- 🤖 Agentic workflow powered by CrewAI
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ FastAPI backend for API communication
- 🎨 Streamlit frontend with chat interface
- 📚 Source document references
- 🛠 Tool usage and reasoning display

---

## 🏗 Project Architecture

```
User
   │
   ▼
Streamlit Frontend
   │
   ▼
FastAPI Backend
   │
   ▼
CrewAI Agent
   │
   ▼
RAG Tool
   │
   ▼
Chroma Vector Database
   │
   ▼
Groq LLM
   │
   ▼
Response + Sources
```

---

## 📁 Project Structure

```
caps-project-3-astrarag-agentic-rag/
│
├── docs_dir/                 # PDF documents
├── Vector_Store_DB/          # Chroma Vector Database
├── src/
│   ├── rag_doc_ingestion/    # Document ingestion pipeline
│   ├── agents_src/           # CrewAI agents, tasks and tools
│   ├── backend_src/          # FastAPI backend
│   └── frontend_src/         # Streamlit frontend
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

- Python
- CrewAI
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM
- FastAPI
- Streamlit
- Pydantic
- python-dotenv

---

## 📄 Document Ingestion

The ingestion pipeline:

- Reads PDF documents
- Splits them into chunks
- Generates embeddings
- Stores vectors in ChromaDB

Run:

```bash
python -m src.rag_doc_ingestion.ingest_docs
```

---

## ▶️ Start Backend

```bash
python -m src.backend_src.main
```

Backend runs at:

```
http://localhost:8000
```

---

## 💻 Start Frontend

```bash
streamlit run src/frontend_src/app.py
```

---

## 🔄 Workflow

1. User enters a question.
2. Streamlit sends the request to FastAPI.
3. FastAPI calls the CrewAI agent.
4. CrewAI invokes the RAG retrieval tool.
5. Relevant document chunks are retrieved from ChromaDB.
6. Groq LLM generates an answer using the retrieved context.
7. The answer, sources, tool information, and rationale are returned to the frontend.

---

## 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
cd caps-project-3-astrarag-agentic-rag
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file containing:

```env
GROQ_API_KEY=your_groq_api_key

MODEL_NAME=llama-3.3-70b-versatile
MODEL_TEMPERATURE=0

DOCUMENTS_DIR=docs_dir
VECTOR_STORE_DIR=Vector_Store_DB
COLLECTION_NAME=astrarag

API_HOST=localhost
API_PORT=8000
```

---

## 📌 Future Improvements

- Multiple document formats
- Conversation memory
- Authentication
- Docker deployment
- Cloud vector database
- Streaming responses

---

## 👨‍💻 Author

Prince

Built as an Agentic RAG project using CrewAI, LangChain, FastAPI, Streamlit, ChromaDB, and Groq.
