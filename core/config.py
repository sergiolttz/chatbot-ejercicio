import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
CO_API_KEY = os.getenv("COHERE_API_KEY")
model = init_chat_model("command-r-plus", model_provider="cohere")

