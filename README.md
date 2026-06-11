# 🧠 Insurance AI Chatbot (RAG System)

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from insurance PDF documents using local LLMs.

---

## 🚀 Features

- PDF-based question answering
- RAG architecture (Retrieval + Generation)
- Semantic search using embeddings
- Local LLM via Ollama
- FastAPI backend

---

## 🏗️ Tech Stack

- FastAPI
- Ollama (Llama 3.2)
- ChromaDB
- Sentence Transformers
- PyPDF

---

## 💻 System Requirements

A new user must have the following on their machine before running this project:

| Requirement | Why it is needed |
|-------------|------------------|
| **Python 3.10 or higher** | Runs the FastAPI app, ingest script, and Python packages |
| **pip** | Installs packages from `requirements.txt` |
| **Ollama** | Runs the local LLM (`llama3.2`) used for answers |
| **Internet (first run only)** | Downloads Python packages and the Ollama model |
| **~2–4 GB free disk space** | For Python packages, embeddings model, and `chroma_db` |

Check that Python and Ollama are installed:

```bash
python --version
pip --version
ollama --version
```

Install Ollama from: https://ollama.com/download

Pull the model used by this project:

```bash
ollama pull llama3.2
```

You also need:

- A **PDF file** in a `data/` folder (see step 3 below)
- **Ollama running** in the background when you use the `/chat` API

---

## 📦 Setup Instructions

### 1. Create virtual environment (recommended)

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies from `requirements.txt`

```bash
pip install -r requirements.txt
```

#### Fix if you get `ModuleNotFoundError` (new users)

`requirements.txt` lists the main packages, but this project also uses **LangChain** libraries in `ingest.py` and `app/rag.py`. If you see errors like:

- `ModuleNotFoundError: No module named 'langchain_community'`
- `ModuleNotFoundError: No module named 'langchain_text_splitters'`

run this **after** `pip install -r requirements.txt`:

```bash
pip install langchain-community langchain-text-splitters
```

To confirm everything is installed:

```bash
pip list | findstr langchain
```

On macOS/Linux, use `grep` instead of `findstr`:

```bash
pip list | grep langchain
```

You should see `langchain-community` and `langchain-text-splitters` in the list.

### 3. Add your PDF document

Create a `data` folder and place your insurance PDF inside it:

```bash
mkdir data
```

Default path expected by `ingest.py`:

```
data/hdfc-life-C2I-n-sanchay-plus.pdf
```

To use a different PDF, change `PDF_PATH` in `ingest.py`.

### 4. Build the vector database

```bash
python ingest.py
```

### 5. Start the server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000/docs to test the API.

### 6. Test the chat endpoint

```bash
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d "{\"question\": \"What is this policy about?\"}"
```

---

## ✅ Quick Checklist for New Users

- [ ] Python 3.10+ installed
- [ ] Virtual environment created and activated
- [ ] `pip install -r requirements.txt` completed
- [ ] `pip install langchain-community langchain-text-splitters` (if import errors appear)
- [ ] Ollama installed and `ollama pull llama3.2` done
- [ ] PDF placed in `data/` folder
- [ ] `python ingest.py` ran successfully
- [ ] `uvicorn app.main:app --reload` running
