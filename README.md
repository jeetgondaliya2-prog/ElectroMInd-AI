# 🤖 ElectroMind AI

### AI-Powered Troubleshooting Assistant using Retrieval-Augmented Generation (RAG)



<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge)
![Mistral AI](https://img.shields.io/badge/Mistral-AI-orange?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-success?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented--Generation-purple?style=for-the-badge)

</p>

---

# 📌 Overview

**ElectroMind AI** is an intelligent **Retrieval-Augmented Generation (RAG)** based troubleshooting assistant developed for both **Software Engineering** and **Electronics & Communication Engineering**.

Instead of relying only on the pretrained knowledge of a Large Language Model (LLM), ElectroMind AI retrieves relevant information from a custom PDF knowledge base before generating responses.

This approach significantly improves answer accuracy, provides source-aware responses, and minimizes hallucinations.

The assistant can answer questions related to:

### 💻 Software

* Python Errors
* SSL Certificate Issues
* Git & GitHub
* Docker
* Networking
* Operating Systems
* Programming Concepts
* Debugging

### 🔌 Electronics

* Arduino
* ESP32
* Raspberry Pi
* Sensors
* Embedded Systems
* IoT
* Microcontrollers
* Digital Electronics
* Circuit Troubleshooting

---

# ✨ Features

* 📄 Custom PDF Knowledge Base
* 🧠 Retrieval-Augmented Generation (RAG)
* 🔍 Semantic Search
* 📚 Chroma Vector Database
* 🤖 Mistral AI Integration
* ⚡ Fast Context Retrieval
* 📖 Source Document References
* 💻 Interactive Streamlit Interface
* 🏗 Modular Project Structure
* 🔐 Environment Variable Support

---

# 🧠 How ElectroMind AI Works

### Step 1 — Document Loading

The application loads all PDF documents from the knowledge base using **PyPDFLoader**.

Each page is converted into a LangChain Document object while preserving metadata.

---

### Step 2 — Document Chunking

Large documents are divided into overlapping chunks using **RecursiveCharacterTextSplitter**.

Why?

* Better retrieval
* Better embeddings
* Preserves context
* Fits LLM context window

---

### Step 3 — Embedding Generation

Each chunk is converted into a vector representation using

> sentence-transformers/all-MiniLM-L6-v2

These embeddings capture semantic meaning instead of keyword matching.

---

### Step 4 — Vector Database

Generated embeddings are stored inside **ChromaDB**.

Instead of reading every PDF repeatedly, ElectroMind AI performs semantic similarity search on vector embeddings.

---

### Step 5 — Semantic Retrieval

When a user asks a question:

* Question → Embedding
* Similarity Search
* Retrieve Top-K Chunks

The retrieved chunks become the context for the LLM.

---

### Step 6 — Prompt Engineering

A structured prompt combines

* Retrieved Context
* User Question

This ensures the model answers based on retrieved knowledge.

---

### Step 7 — Response Generation

The final prompt is sent to **Mistral AI**.

The assistant returns:

* Context-aware answer
* Step-by-step explanation
* Troubleshooting guide
* Source document references

---

# 💻 Tech Stack

## Programming Language

* Python

## AI / LLM

* Mistral AI

## Framework

* LangChain

## Vector Database

* ChromaDB

## Embedding Model

* HuggingFace
* sentence-transformers/all-MiniLM-L6-v2

## Frontend

* Streamlit

## Document Processing

* PyPDFLoader

## Environment Management

* python-dotenv

---

# 📂 Project Structure

```text
ElectroMind-AI/
│
├── app.py                     # Streamlit User Interface
├── rag.py                     # Retrieval & LLM Pipeline
├── ingest.py                  # Build Chroma Vector Database
├── config.py                  # Configuration
├── test_llm.py                # Test Mistral API
│
├── utils/
│   ├── loader.py              # PDF Loader
│   ├── splitter.py            # Text Chunking
│   ├── embeddings.py          # Embedding Model
│   ├── prompts.py             # Prompt Templates
│   └── helper.py              # Utility Functions (optional)
│
├── knowledge_base/
│   ├── software/
│   └── electronics/
│
├── vector_db/                 # Generated Chroma Database
│
├── assets/
│   └── system_architecture.png
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ElectroMind-AI.git

cd ElectroMind-AI
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a **.env** file

```env
MISTRAL_API_KEY=your_api_key_here
```

---

# 📥 Build Vector Database

Place your PDFs inside

```text
knowledge_base/
```

Run

```bash
python ingest.py
```

This creates

```text
vector_db/
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

---

# 💬 Example Questions

### Software

* Why am I getting ModuleNotFoundError?
* SSL Certificate Verification Failed
* Git merge conflict
* Docker container not starting
* Python package cannot be imported

### Electronics

* Arduino is not detected
* ESP32 COM port missing
* LED is not glowing
* Sensor not responding
* Ultrasonic sensor giving wrong readings

---

# 📚 Concepts Implemented

* Retrieval-Augmented Generation (RAG)
* LangChain Pipelines
* Prompt Engineering
* Semantic Search
* Vector Embeddings
* ChromaDB
* Similarity Search
* Document Chunking
* Document Retrieval
* LLM Integration
* Streamlit Deployment
* Modular AI Application Design

---

# 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

* Building an end-to-end RAG application
* Processing and indexing PDF documents
* Implementing semantic search using embeddings
* Designing and querying vector databases
* Creating modular AI architectures
* Prompt engineering for grounded responses
* Integrating LangChain with Mistral AI
* Developing interactive AI applications using Streamlit

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork this repository, create a new branch, and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ If you found this project helpful...

Please consider giving this repository a **Star ⭐** to support the project and help others discover it.
