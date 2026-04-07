import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from crewai import LLM
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    GROQ_API_KEY: str


    @property
    def MODEL_FLASH(self):
        return LLM(
            model="gemini/gemini-2.5-flash",
            api_key=self.GEMINI_API_KEY,
            temperature=0.6
        )
    
    @property
    def MODEL_PRO(self):
        return LLM(
            model="gemini/gemini-2.5-flash",
            api_key=self.GEMINI_API_KEY,
            temperature=0.0
        )
    

    @property
    def MODEL_GROQ(self):
        return LLM(
            model="groq/llama-3.3-70b-versatile",
            api_key=self.GROQ_API_KEY,
            temperature=0.0
        )
    
    model_config = SettingsConfigDict(env_file=".env")

    agent_instances:Dict[str,Any]={}


settings = Settings()