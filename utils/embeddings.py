from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model(): 
    """
    Create and return the embedding model.
    """

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model


if __name__ == "__main__":

    embedding = get_embedding_model()

    vector = embedding.embed_query("Arduino is not detected")

    print(f"Vector Dimension: {len(vector)}")
    print(vector[:10])
