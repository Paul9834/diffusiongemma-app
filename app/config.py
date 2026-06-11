import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("VLLM_BASE_URL", "http://127.0.0.1:8000/v1")
    api_key: str = os.getenv("VLLM_API_KEY", "EMPTY")
    model_id: str = os.getenv("VLLM_MODEL_ID", "google/diffusiongemma-26B-A4B-it")
    host: str = os.getenv("APP_HOST", "127.0.0.1")
    port: int = int(os.getenv("APP_PORT", "7860"))

settings = Settings()
