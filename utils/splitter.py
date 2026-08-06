from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into smaller chunks. 
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Total Chunks Created: {len(chunks)}")

    return chunks


if __name__ == "__main__":

    from loader import load_documents

    docs = load_documents()

    chunks = split_documents(docs)

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content[:500])
