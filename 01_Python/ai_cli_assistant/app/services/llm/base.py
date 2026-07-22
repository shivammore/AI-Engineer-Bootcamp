from abc import ABC, abstractmethod


class LLMService(ABC):
    """Interface implemented by every LLM provider."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a text response for a user prompt."""