import sys

from loguru import logger as logger_
from loguru._logger import Logger


def configure_logger() -> Logger:
    logger_.remove()
    logger_.add(
        sys.stdout,
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        enqueue=True,
        backtrace=True,
        diagnose=True,
    )
    return logger_  # type: ignore[return-value]


logger = configure_logger()
