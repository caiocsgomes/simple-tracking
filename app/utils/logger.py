import logging
import os
import sys

FORMATTER = logging.Formatter(
    "%(levelname)s — %(asctime)s — %(name)s — %(message)s")

standard_log_level = int(os.getenv("APP_LOG_LEVEL")) or 10  # 10 = debug


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(standard_log_level)
    logger.addHandler(get_console_handler())
    logger.propagate = False
    return logger
