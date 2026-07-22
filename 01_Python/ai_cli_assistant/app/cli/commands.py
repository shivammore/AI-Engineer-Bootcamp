import argparse
from collections.abc import Callable

from app.config import settings
from app.logger import get_logger

logger = get_logger(__name__)


def handle_version(_: argparse.Namespace) -> None:
    """Display the application version."""
    logger.info("Version command executed")
    print(f"{settings.app_name} version 0.1.0")


def handle_health(_: argparse.Namespace) -> None:
    """Check local application readiness."""
    logger.info("Health command executed")

    checks = {
        "application": "healthy",
        "logging": "healthy",
        "openai_key": (
            "configured"
            if settings.openai_api_key
            else "missing"
        ),
    }

    for check, result in checks.items():
        print(f"{check}: {result}")


def handle_config(_: argparse.Namespace) -> None:
    """Display non-sensitive application configuration."""
    logger.info("Config command executed")

    print(f"Application name: {settings.app_name}")
    print(f"Log level: {settings.log_level}")


def handle_chat(_: argparse.Namespace) -> None:
    """Start an interactive AI chat session."""
    from app.services.llm.openai_service import (
        LLMServiceError,
        OpenAIService,
    )

    logger.info("Chat command started")

    try:
        llm_service = OpenAIService()
    except (ValueError, LLMServiceError) as exc:
        logger.error("Could not initialize LLM service: %s", exc)
        print(f"Configuration error: {exc}")
        return

    print(f"Welcome to {settings.app_name}")
    print("Type 'exit' to close the chat.")

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Please enter a message.")
            continue

        if user_input.lower() in {"exit", "quit"}:
            logger.info("Chat command stopped")
            print("Assistant: Goodbye!")
            break

        try:
            response = llm_service.generate(user_input)
            print(f"\nAssistant: {response}")

        except LLMServiceError as exc:
            logger.error("Chat request failed: %s", exc)
            print(f"\nAssistant error: {exc}")


def register_command(
    subparsers: argparse._SubParsersAction,
    *,
    name: str,
    description: str,
    handler: Callable[[argparse.Namespace], None],
) -> None:
    """Register a CLI subcommand and its handler."""
    parser = subparsers.add_parser(name, help=description)
    parser.set_defaults(handler=handler)


def build_parser() -> argparse.ArgumentParser:
    """Create and configure the root argument parser."""
    parser = argparse.ArgumentParser(
        prog="astra",
        description="Project Astra AI CLI Assistant",
    )

    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
    )

    register_command(
        subparsers,
        name="version",
        description="Show the application version",
        handler=handle_version,
    )

    register_command(
        subparsers,
        name="health",
        description="Check application health",
        handler=handle_health,
    )

    register_command(
        subparsers,
        name="config",
        description="Show non-sensitive configuration",
        handler=handle_config,
    )

    register_command(
        subparsers,
        name="chat",
        description="Start the chat interface",
        handler=handle_chat,
    )

    return parser


def run_cli() -> None:
    """Parse CLI arguments and execute the selected command."""
    parser = build_parser()
    args = parser.parse_args()

    if not hasattr(args, "handler"):
        parser.print_help()
        return

    try:
        args.handler(args)
    except KeyboardInterrupt:
        logger.warning("Command interrupted by the user")
        print("\nOperation cancelled.")
    except Exception:
        logger.exception("Unexpected CLI failure")
        print("An unexpected error occurred. Check the logs for details.")