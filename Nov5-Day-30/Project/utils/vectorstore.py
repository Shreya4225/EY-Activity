"""
Vectorstore utilities: build embeddings, split documents, and create or load a Chroma/FAISS store.
"""

import os
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_core.documents import Document

CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIRECTORY", "./.chromadb")


def create_embeddings():
    """Create and return an embeddings object. Swap to HuggingFaceEmbeddings if needed."""
    return OpenAIEmbeddings()


def split_documents(docs: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
    """Use RecursiveCharacterTextSplitter to split long documents into chunks."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)


def build_vectorstore_from_documents(docs: List[Document], persist: bool = True, collection_name: str = "code_explainer") -> Chroma:
    """Build a Chroma vectorstore from a list of LangChain Documents. Returns the Chroma instance."""
    embeddings = create_embeddings()

    persist_directory = CHROMA_PERSIST_DIR if persist else None

    vectordb = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory, collection_name=collection_name)
    if persist and persist_directory:
        vectordb.persist()
    return vectordb


def load_or_create_vectorstore(docs: List[Document], persist: bool = True, collection_name: str = "code_explainer") -> Chroma:
    """If a persistent store exists, load it; otherwise create a new one.
    For simplicity this function always recreates the collection for the provided docs.
    """
    return build_vectorstore_from_documents(docs, persist=persist, collection_name=collection_name)