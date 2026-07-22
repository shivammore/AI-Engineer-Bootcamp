from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    OpenAI,
    RateLimitError,
)

from app.config import settings
from app.logger import get_logger
from app.services.llm.base import LLMService

logger = get_logger(__name__)


class LLMServiceError(RuntimeError):
    """Raised when the configured LLM provider cannot complete a request."""


class OpenAIService(LLMService):
    def __init__(self) -> None:
        settings.validate_openai()

        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    def generate(self, prompt: str) -> str:
        cleaned_prompt = prompt.strip()

        if not cleaned_prompt:
            raise ValueError("Prompt cannot be empty.")

        logger.info(
            "Sending request to OpenAI using model %s",
            self.model,
        )

        try:
            response = self.client.responses.create(
                model=self.model,
                instructions=(
                    "You are Project Astra, a clear and helpful AI assistant. "
                    "Give concise, accurate answers."
                ),
                input=cleaned_prompt,
            )

            answer = response.output_text.strip()

            if not answer:
                raise LLMServiceError(
                    "The model returned an empty response."
                )

            logger.info("OpenAI response received")
            return answer

        except AuthenticationError as exc:
            logger.error("OpenAI authentication failed")
            raise LLMServiceError(
                "Authentication failed. Check OPENAI_API_KEY."
            ) from exc

        except RateLimitError as exc:
            logger.warning("OpenAI rate limit reached")
            raise LLMServiceError(
                "The service is temporarily rate-limited. Try again later."
            ) from exc

        except APIConnectionError as exc:
            logger.error("Could not connect to OpenAI")
            raise LLMServiceError(
                "Could not connect to the AI provider."
            ) from exc

        except APIStatusError as exc:
            logger.error(
                "OpenAI API returned status %s",
                exc.status_code,
            )
            raise LLMServiceError(
                f"The AI provider returned status {exc.status_code}."
            ) from exc