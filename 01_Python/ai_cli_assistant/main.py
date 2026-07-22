from app.cli.commands import run_cli
from app.logger import get_logger

logger = get_logger(__name__)


def main() -> None:
    logger.info("Application started")
    run_cli()
    logger.info("Application stopped")


if __name__ == "__main__":
    main()