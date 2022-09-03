import logging.handlers
import config as cfg
import sys

formatter = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(funcName)s: %(message)s")

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(filename=cfg.LOGGING_FILENAME,
                                   mode="a",
                                   encoding="utf-8")
file_handler.setFormatter(formatter)

logger = logging.getLogger("Main Logger")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
