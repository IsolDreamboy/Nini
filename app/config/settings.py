import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    GROQ_API_KEY: str

    @property
    def MODEL_FLASH(self) -> ChatGoogleGenerativeAI:
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=self.GEMINI_API_KEY,
            temperature=0.6
        )
    
    @property
    def MODEL_PRO(self) -> ChatGoogleGenerativeAI:
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=self.GEMINI_API_KEY,
            temperature=0.0
        )

    @property
    def MODEL_GROQ(self) -> ChatGroq:
        return ChatGroq(
            model="llama-3.3-70b-versatile",
            groq_api_key=self.GROQ_API_KEY,
            temperature=0.0
        )
    
    model_config = SettingsConfigDict(env_file=".env")

    agent_instances: Dict[str, Any] = {}


settings = Settings()