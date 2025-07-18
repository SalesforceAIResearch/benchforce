import logging
import os


class MsecFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)
        self.default_msec_format = '%s.%03d'


def get_log_level(name: str):
    named_log_level_env_var = f"LOG_LEVEL_{name.upper()}"
    if named_log_level_env_var in os.environ:
        return logging.getLevelNamesMapping()[os.environ[named_log_level_env_var]]
    return logging.getLevelNamesMapping()[os.environ.get("LOG_LEVEL", "INFO")]


def make_logger(name: str, level: int | None = None):
    if level is None:
        level = get_log_level(name=name)

    logger = logging.getLogger(name=name)
    logger.setLevel(level=level)
    ch = logging.StreamHandler()
    ch.setLevel(level=level)
    formatter = MsecFormatter('%(asctime)s %(levelname).1s %(name)s | %(message)s')
    ch.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(ch)
    logger.propagate = False  # Prevent propagation to root logger
    return logger
