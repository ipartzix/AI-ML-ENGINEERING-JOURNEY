import logging


def setup_logger(log_file: str = "app.log"):
    """
    Configure logging for the project.
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("Logger initialized. - utils.py:13")


def print_separator():
    print("= - utils.py:17" * 50)