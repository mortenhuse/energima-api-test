import logging
from datetime import datetime


def configure_logger(logger_name: str, log_level: str, logger_file):
    """
    Configure logger
    :param logger_name: Name of the logger. None for root logger.
    :param logger_file: Name of text file E.G. "myloggfile"
    :param log_level: Log level. E.g. "DEBUG"
    :return: Logger
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    fh = logging.FileHandler(logger_file)
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.info("---Logger started---")
    return logger
