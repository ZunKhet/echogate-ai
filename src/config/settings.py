import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"


settings = Settings()
