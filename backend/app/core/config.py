import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")

    JINA_API_KEY: str = os.getenv("JINA_API_KEY", "")

    FRONTEND_URL: str = os.getenv(
        "FRONTEND_URL",
        "http://localhost:5173",
    )

    AUTH_URL: str = os.getenv(
        "AUTH_URL",
        "http://localhost:3000",
    )


settings = Settings()