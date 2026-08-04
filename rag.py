import os
import streamlit as st
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

api_key = st.secrets.get("MISTRAL_API_KEY", os.getenv("MISTRAL_API_KEY"))

# -------------------------------------------------
# Load Environment Variables
# -------------------------------------------------



# -------------------------------------------------
# Embedding Model
# -------------------------------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

# -------------------------------------------------
# Load Chroma Database
# -------------------------------------------------

vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_model
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": 4}
)

# -------------------------------------------------
# Mistral Model
# -------------------------------------------------

llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0,
    api_key=api_key,
    max_retries=0
)

# -------------------------------------------------
# Prompt
# -------------------------------------------------

prompt = ChatPromptTemplate.from_template("""
You are an expert AI Troubleshooting Assistant.

Answer the user's question using the retrieved context.

Rules:
1. If the context contains the answer, explain it clearly.
2. Give step-by-step troubleshooting whenever possible.
3. If the context is partially relevant, still try to help using that information.
4. Only say "I couldn't find relevant information in the knowledge base." if the retrieved context is completely unrelated.

Retrieved Context:
{context}

Question:
{question}

Answer:
""")

parser = StrOutputParser()

# -------------------------------------------------
# Main Function
# -------------------------------------------------


def ask_question(question):

    # Retrieve documents
    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    # Debug (remove later if you want)
    print("\n" + "=" * 80)
    print("RETRIEVED CONTEXT")
    print("=" * 80)
    print(context[:2000])      # Print first 2000 characters
    print("=" * 80)

    chain = prompt | llm | parser

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return answer, docs


# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__ == "__main__":

    print("=" * 70)
    print("AI Troubleshooting Assistant")
    print("=" * 70)

    while True:

        query = input("\nAsk Question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        answer, docs = ask_question(query)

        print("\n")
        print("=" * 70)
        print("ANSWER")
        print("=" * 70)
        print(answer)

        print("\n")
        print("=" * 70)
        print("SOURCES")
        print("=" * 70)

        sources = set()

        for doc in docs:
            sources.add(doc.metadata["source"])

        for source in sources:
            print(source)