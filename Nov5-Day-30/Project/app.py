"""
Streamlit front-end for the Code Explainer.

- Upload single files (.py, .js, .cpp) or a zipped folder.
- Index uploaded code into Chroma using OpenAI embeddings.
- Ask questions; get explanations with multi-turn memory.
"""
import os
import streamlit as st
import tempfile
import shutil
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_core.documents import Document

from utils.loader import save_uploaded_file, extract_zip, build_loader_from_path, collect_file_paths
from utils.vectorstore import split_documents, load_or_create_vectorstore
from utils.llm_chain import create_conversational_chain


import os
import streamlit as st
import tempfile
import shutil
from pathlib import Path
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.schema import Document
from langchain.document_loaders import DirectoryLoader

from utils.loader import save_uploaded_file, extract_zip, build_loader_from_path, collect_file_paths
from utils.vectorstore import split_documents, load_or_create_vectorstore
from utils.llm_chain import create_conversational_chain

# Load environment variables (OPENAI_API_KEY expected)
load_dotenv()

st.set_page_config(page_title="Code Explainer", layout="wide")

st.title("🧠 Code Explainer — Streamlit + LangChain")

# Sidebar: Upload
st.sidebar.header("Upload code")
uploaded = st.sidebar.file_uploader("Upload a .py/.js/.cpp file or a zipped folder", type=["py", "js", "cpp", "zip"], accept_multiple_files=False)

# Persisted objects in session_state
if "vectordb" not in st.session_state:
    st.session_state.vectordb = None
if "chain" not in st.session_state:
    st.session_state.chain = None

# A small helper to index uploaded file(s)
def index_upload(uploaded_file):
    tmpdir = tempfile.mkdtemp()
    try:
        if uploaded_file.name.lower().endswith(".zip"):
            zip_path = os.path.join(tmpdir, uploaded_file.name)
            save_uploaded_file(uploaded_file, zip_path)
            extract_zip(zip_path, tmpdir)
            # collect code file paths
            file_paths = collect_file_paths(tmpdir)
            docs = []
            for p in file_paths:
                loader = TextLoader(p, encoding="utf-8")
                docs.extend(loader.load())
        else:
            file_path = os.path.join(tmpdir, uploaded_file.name)
            save_uploaded_file(uploaded_file, file_path)
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()

        # Add metadata (filename) to each doc
        for d in docs:
            # ensure metadata exists
            if not d.metadata:
                d.metadata = {}
            d.metadata["source_file"] = os.path.basename(d.metadata.get("source", "uploaded_file"))

        # Split docs into chunks
        chunks = split_documents(docs, chunk_size=800, chunk_overlap=100)

        # Build vectorstore (persisted by default)
        vectordb = load_or_create_vectorstore(chunks, persist=True, collection_name="code_explainer")

        # Create retriever and chain
        retriever = vectordb.as_retriever(search_kwargs={"k": 5})
        chain = create_conversational_chain(retriever)



        # Save in session state
        st.session_state.vectordb = vectordb
        st.session_state.chain = chain

        st.success("Indexing complete. You can start asking questions.")
    except Exception as e:
        st.error(f"Indexing failed: {e}")
    finally:
        # cleanup temporary dir
        try:
            shutil.rmtree(tmpdir)
        except Exception:
            pass

# Index button
if uploaded is not None:
    if st.sidebar.button("Index uploaded file/folder"):
        index_upload(uploaded)

# Main area: Query box and results
st.subheader("Ask about your code")

if st.session_state.chain:
    query = st.text_input("💬 Enter your question:", placeholder="e.g., Explain this function or Summarize this file")

    if st.button("Ask"):
        with st.spinner("Analyzing your code..."):
            response = st.session_state.chain.invoke({"question": query})
            st.markdown("### 🤖 Explanation")
            st.write(response["answer"])
else:
    st.info("Please upload and index a file first.")
