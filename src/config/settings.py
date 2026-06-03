import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")
    AI_PROVIDER: str = os.getenv("AI_PROVIDER", "fake")


settings = Settings()
