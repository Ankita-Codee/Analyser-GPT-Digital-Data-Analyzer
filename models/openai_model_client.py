from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL_OPENAI
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = "YOUR OPENAI API KEY HERE"

def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model=MODEL_OPENAI,
        api_key=OPENAI_API_KEY
    )

    return openai_model_client