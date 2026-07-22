import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.app_name = os.getenv("APP_NAME", "AI CLI Assistant")
        self.log_level = os.getenv("LOG_LEVEL", "INFO").upper()

        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-5.6")

    def validate_openai(self) -> None:
        if not self.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. Add it to your environment."
            )


settings = Settings()