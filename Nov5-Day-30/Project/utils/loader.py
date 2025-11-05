"""
Utilities to load single files or directories (zipped) into LangChain loaders.
Supports .py, .js, .cpp, and generic text files.
"""
import os
import zipfile
from typing import List
from langchain_community.document_loaders import TextLoader, DirectoryLoader

# Allowed code extensions
ALLOWED_EXTS = {".py", ".js", ".cpp", ".c", ".h", ".txt"}


def save_uploaded_file(uploaded_file, dest_path: str) -> str:
    """Save a Streamlit uploaded file (uploaded_file) to dest_path and return path."""
    with open(dest_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return dest_path


def extract_zip(zip_path: str, extract_to: str) -> None:
    """Extract a zip file to the target directory."""
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_to)


def build_loader_from_path(path: str):
    """Return a LangChain loader for a file or directory.

    If path is a file -> TextLoader
    If path is a directory -> DirectoryLoader filtering allowed extensions
    """
    if os.path.isfile(path):
        # single file
        return TextLoader(path, encoding="utf-8")
    elif os.path.isdir(path):
        # directory -> load only allowed extensions
        def _ext_filter(file_path: str) -> bool:
            _, ext = os.path.splitext(file_path)
            return ext.lower() in ALLOWED_EXTS

        return DirectoryLoader(
            path,
            glob="**/*",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
            recursive=True,
        )
    else:
        raise ValueError(f"Path not found: {path}")


def collect_file_paths(root_dir: str) -> List[str]:
    """Return list of allowed code file paths under root_dir."""
    files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for fn in filenames:
            _, ext = os.path.splitext(fn)
            if ext.lower() in ALLOWED_EXTS:
                files.append(os.path.join(dirpath, fn))
    return files


