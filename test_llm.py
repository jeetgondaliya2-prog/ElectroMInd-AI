from dotenv import load_dotenv
import os

from langchain_mistralai import ChatMistralAI

load_dotenv()
 
model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7,
    api_key=os.getenv("MISTRAL_API_KEY")
)

response = model.invoke("Say hello in one sentence.")

print(response.content)
