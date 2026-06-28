from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class agentsettings(BaseSettings):
    GROQ_API_KEY: str
    DOCUMENTS_DIR: str
    VECTOR_STORE_DIR: str
    GROQ_MODEL_NAME: str
    MODEL_TEMPERATURE: float

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

