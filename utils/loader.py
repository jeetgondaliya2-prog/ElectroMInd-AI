from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

 
def load_documents():
    """
    Load all PDFs from the knowledge_base folder.
    Returns:
        List[Document]
    """

    # Project Root
    project_root = Path(__file__).resolve().parent.parent

    # knowledge_base folder
    knowledge_base = project_root / "knowledge_base"

    print(f"Project Root      : {project_root}")
    print(f"Knowledge Base    : {knowledge_base}")

    # Check if folder exists
    if not knowledge_base.exists():
        raise FileNotFoundError(
            f"\n❌ Folder not found:\n{knowledge_base}\n"
            "Create a folder named 'knowledge_base' in your project root."
        )

    # Find all PDFs recursively
    pdf_files = list(knowledge_base.rglob("*.pdf"))

    if len(pdf_files) == 0:
        print("\n❌ No PDF files found inside knowledge_base.")
        return []

    print(f"\n📄 Found {len(pdf_files)} PDF(s)\n")

    documents = []

    for pdf in pdf_files:
        print(f"Loading -> {pdf.name}")

        loader = PyPDFLoader(str(pdf))
        docs = loader.load()

        documents.extend(docs)

    print("\n====================================")
    print(f"✅ Total Pages Loaded : {len(documents)}")
    print("====================================\n")

    return documents


if __name__ == "__main__":

    docs = load_documents()

    if docs:
        print("First Page Preview:\n")
        print("-" * 50)
        print(docs[0].page_content[:500])
        print("-" * 50)
    else:
        print("No documents loaded.")
