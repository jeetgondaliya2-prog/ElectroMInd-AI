from pathlib import Path
import shutil

from langchain_chroma import Chroma

from utils.loader import load_documents
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model


def create_vector_database(): 
    print("=" * 60)
    print("🚀 Building Vector Database")
    print("=" * 60)

    # 1. Load PDFs
    print("\n📂 Loading documents...")
    documents = load_documents()

    if not documents:
        print("❌ No documents found.")
        return

    # 2. Split documents
    print("\n✂ Splitting documents...")
    chunks = split_documents(documents)

    # 3. Load embedding model
    print("\n🧠 Loading embedding model...")
    embedding_model = get_embedding_model()

    # 4. Vector DB location
    persist_directory = "vector_db"

    # Delete old database (optional)
    if Path(persist_directory).exists():
        print("\n🗑 Removing old vector database...")
        shutil.rmtree(persist_directory)

    # 5. Create Chroma database
    print("\n💾 Creating Chroma Vector Database...")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
    )

    print("\n" + "=" * 60)
    print("✅ Vector Database Created Successfully!")
    print(f"📁 Saved in: {persist_directory}")
    print(f"📄 Total Chunks: {len(chunks)}")
    print("=" * 60)

    return vector_db


if __name__ == "__main__":
    create_vector_database()
