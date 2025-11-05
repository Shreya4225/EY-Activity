# 🧠 Code Explainer — AI-Powered Code Understanding Tool

The **Code Explainer** is an intelligent application that allows users to upload their source code (or zip folders), automatically index it using **LangChain**, and then **chat with their code** to understand its logic, structure, and behavior — just like having an AI code reviewer or mentor.

This project uses **OpenRouter (or OpenAI)** models integrated with **LangChain**, **Chroma vector database**, and **Streamlit** for an interactive UI.

---

## 🚀 Features

- 📂 **Upload Files or Folders**
  - Supports `.py`, `.js`, `.cpp`, `.c`, `.h`, and `.txt` files
  - Accepts both single files and zipped projects

- 🧩 **Automatic Code Indexing**
  - Splits code into manageable chunks
  - Creates vector embeddings using `OpenAIEmbeddings`
  - Stores them in a **ChromaDB** vector store for efficient retrieval

- 💬 **Chat with Your Code**
  - Asks questions like:
    > “What does this function do?”  
    > “How are database connections handled?”  
    > “Which part of the code initializes the API?”

- 🔄 **Memory-Aware Conversations**
  - Remembers previous context using `ConversationBufferMemory`
  - Provides smoother, contextual follow-up answers

- 🌐 **Supports OpenRouter API**
  - Compatible with OpenAI or OpenRouter endpoints  
  - Default model: `gpt-4o-mini`

---

## 🧠 Tech Stack

| Component | Technology Used | Purpose |
|------------|----------------|----------|
| **Frontend/UI** | Streamlit | User interface for file upload and chat |
| **Backend Engine** | Python | Core logic, model integration, and data handling |
| **LLM Framework** | LangChain | Handles retrieval, memory, and chain orchestration |
| **Model Provider** | OpenRouter / OpenAI | Provides the language model for explanations |
| **Embeddings** | OpenAIEmbeddings | Converts text into numerical vectors |
| **Vector Database** | ChromaDB | Stores and retrieves semantically similar code chunks |
| **Environment Management** | Python-dotenv | Loads environment variables securely |

---

## ⚙️ Project Flow (Architecture Overview)

Below is the high-level architecture of how **Code Explainer** works end-to-end:

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


**Summary of Flow:**
1. User uploads source code or zip → handled by `loader.py`.
2. Code is split into chunks → embedded using `OpenAIEmbeddings`.
3. Embeddings stored in **ChromaDB**.
4. When a user asks a question:
   - Retriever fetches relevant code snippets.
   - LLM (`ChatOpenAI`) analyzes them.
   - Response is generated with context and memory.
5. Streamlit displays results interactively.

---


