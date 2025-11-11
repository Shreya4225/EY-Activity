# 🧠 Code Explainer — AI-Powered Code Understanding Tool

## Index

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Workflow](#project-workflow)
- [Key Components](#key-components)
- [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Overview

The **Code Explainer** is an intelligent application designed to help users understand their source code easily. Users can upload individual source files or zipped projects, after which the system automatically indexes the code using **LangChain**. The core feature allows users to **chat with their code**, querying for explanations on logic, structure, and behavior—as if interacting with an AI mentor or code reviewer.

This project integrates state-of-the-art technologies, including **OpenRouter (or OpenAI)** language models through **LangChain**, a **Chroma vector database** for semantic retrieval, and **Streamlit** for a sleek interactive user interface.

---

## Problem Statement

Understanding complex and unfamiliar source code can be time-consuming and difficult, especially for large projects or legacy codebases. Developers often need to manually read through code files and piece together functionality from scattered implementations. The **Code Explainer** addresses this challenge by providing an AI-powered assistant capable of comprehending and explaining code on demand, significantly reducing onboarding and review times.

---

## Features

- 📂 **Upload Files or Folders**
  - Supports multiple file types including `.py`, `.js`, `.cpp`, `.c`, `.h`, and `.txt`.
  - Accepts both single source files and zipped project directories for flexibility.

- 🧩 **Automatic Code Indexing**
  - Splits uploaded code into manageable chunks for efficient processing.
  - Generates semantic embeddings using `OpenAIEmbeddings`.
  - Stores embeddings in a **ChromaDB** vector database, enabling fast and relevant retrieval.

- 💬 **Chat with Your Code**
  - Ask targeted questions such as:
    > “What does this function do?”  
    > “How are database connections handled?”  
    > “Which part of the code initializes the API?”

- 🔄 **Memory-Aware Conversations**
  - Maintains prior conversation context with `ConversationBufferMemory` for coherent follow-ups.
  - Enhances user experience by providing more natural, context-sensitive answers.

- 🌐 **Supports OpenRouter API**
  - Fully compatible with OpenAI or OpenRouter endpoints.
  - Default large language model set to `gpt-4o-mini` for optimal performance.

---

## Project Structure

├── app.py # Streamlit frontend UI
├── utils/
│ ├── loader.py # File upload, extraction, and text loading utilities
│ ├── vectorstore.py # Code chunk splitting and embedding creation logic
│ ├── llm_chain.py # LangChain conversational chain with memory and retrieval
├── README.md # This project documentation
├── requirements.txt # Python dependencies
├── .env # Environment variables for API keys and configs
└── data/ # Persistent storage for vector database and uploa


## Tech Stack

| Component           | Technology Used    | Purpose                                      |
|---------------------|-------------------|----------------------------------------------|
| **Frontend/UI**      | Streamlit         | User interface for uploading files and chatting with code |
| **Backend Engine**   | Python            | Core application logic, file processing, API integration |
| **LLM Framework**    | LangChain         | Retrieval augmented generation, conversation memory |
| **Model Provider**   | OpenRouter/OpenAI | Large language models for code explanation and interaction |
| **Embeddings**       | OpenAIEmbeddings  | Converts code text into vector embeddings    |
| **Vector Database**  | ChromaDB          | Stores code embeddings and enables semantic search |
| **Environment Management** | Python-dotenv  | Securely loads environment variables         |

---

## Configuration

- Rename `.env.example` to `.env`.
- Update `.env` with your API keys and configuration:
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
LOG_FILE=llm_app.log

text
- Ensure sufficient permissions to create and write to `data/` directory for storing vector DB.

---

## Usage

1. Start the Streamlit app (frontend UI):
streamlit run app.py

text

2. Upload your source file or zipped project through the UI.

3. Ask questions about the uploaded code in the chat interface.

4. The system will retrieve relevant context and provide AI-generated explanations interactively.

---

## Project Workflow

**Architecture Overview:**

text
     ┌────────────────────────────┐
     │        User Uploads        │
     │ .py / .js / .cpp / .zip    │
     └────────────┬───────────────┘
                  │
                  ▼
      ┌──────────────────────────┐
      │      File Handling       │
      │ utils/loader.py          │
      │ → Save file              │
      │ → Extract zip (if any)   │
      │ → Load text content      │
      └────────────┬─────────────┘
                  │
                  ▼
      ┌──────────────────────────┐
      │    Text Splitting        │
      │ utils/vectorstore.py     │
      │ → Split into chunks      │
      │ → Create embeddings      │
      │ → Store in ChromaDB      │
      └────────────┬─────────────┘
                  │
                  ▼
      ┌──────────────────────────┐
      │ Conversational Chain     │
      │ utils/llm_chain.py       │
      │ → ChatOpenAI model       │
      │ → Memory via LangChain   │
      │ → Retrieval mechanism    │
      └────────────┬─────────────┘
                  │
                  ▼
     ┌────────────────────────────┐
     │         Streamlit UI       │
     │  app.py                    │
     │ → Ask questions            │
     │ → Retrieve code context    │
     │ → Display AI explanations  │
     └────────────────────────────┘
text

This end-to-end flow enables users to interactively query complex codebases with AI assistance.

---

## Key Components

- **`loader.py`** — Handles uploads, saves files, extracts zipped archives, and loads textual content.
- **`vectorstore.py`** — Splits code texts into chunks, creates vector embeddings, and manages the ChromaDB index.
- **`llm_chain.py`** — Implements the LangChain conversational logic, integrates memory, and manages retrieval.
- **`app.py`** — Streamlit UI for file upload and chat interaction with the AI-powered code understanding engine.

---

## API Documentation

The primary API endpoints and usage:

- **POST `/process`**  
  Accepts a JSON payload:
{
"text": "your query here"
}

text
Returns:
{
"input": "your query here",
"result": "AI generated answer related to code"
}

text

- Supports queries about uploaded code, such as function details, code flow, specific file contents, or architecture explanations.

---

## Troubleshooting

- **Common Issue: API Key Errors**  
Ensure `OPENROUTER_API_KEY` in `.env` is valid and correctly loaded.

- **No answers or blank output**  
Confirm the uploaded files are supported and properly indexed.

- **Installation issues**   
Verify all dependencies are installed; use `pip install -r requirements.txt`.

- **File upload problems**  
Check file size limits and zip archive integrity.

For detailed logs, review the `llm_app.log` file as configured.

---

## Contributing

Contributions and improvements are welcome! To contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a pull request explaining your changes.

Please adhere to the existing code style and write tests where relevant.