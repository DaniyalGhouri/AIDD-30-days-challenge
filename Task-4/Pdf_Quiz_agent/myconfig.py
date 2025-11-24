from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# print("Using Gemini API Key:", GEMINI_API_KEY)
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",)

MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client,)

config = RunConfig(
    model=MODEL,
    model_provider=external_client,
    tracing_disabled=True,
) 
