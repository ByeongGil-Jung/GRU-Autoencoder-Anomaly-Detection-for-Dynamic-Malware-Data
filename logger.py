from pathlib import Path
import logging
import os
import pathlib


class Logger(object):
    __INSTANCE = None

    LOG_DIRECTORY_PATH = os.path.join(pathlib.Path(__file__).parent.absolute(), "log")
    LOG_FILE_NAME = "logging.log"

    @classmethod
    def __get_instance(cls):
        return cls.__INSTANCE

    @classmethod
    def instance(cls, *args, **kwargs):
        cls.__INSTANCE = cls(*args, **kwargs)
        cls.instance = cls.__get_instance
        return cls.__INSTANCE

    def __init__(self, log_level="debug"):
        self.logger = logging.getLogger(__name__)
        self.init_logger()
        self.set_log_level(log_level=log_level)

    def init_logger(self):
        Path(self.LOG_DIRECTORY_PATH).mkdir(parents=True, exist_ok=True)

        log_stream_handler = logging.StreamHandler()
        log_file_handler = logging.FileHandler(os.path.join(self.LOG_DIRECTORY_PATH, self.LOG_FILE_NAME))

        log_formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)s] %(message)s")

        log_stream_handler.setFormatter(log_formatter)
        log_file_handler.setFormatter(log_formatter)

        self.logger.addHandler(log_stream_handler)
        self.logger.addHandler(log_file_handler)

    def set_log_level(self, log_level: str):
        if log_level == "info":
            self.logger.setLevel(level=logging.INFO)
        elif log_level == "debug":
            self.logger.setLevel(level=logging.DEBUG)
        elif log_level == "error":
            self.logger.setLevel(level=logging.ERROR)
        elif log_level == "warning":
            self.logger.setLevel(level=logging.WARNING)


logger = Logger.instance().logger
