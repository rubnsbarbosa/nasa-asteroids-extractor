import sys
import logging


class LoggingUtils:
    @staticmethod
    def config_logger(name):
        logging.basicConfig(
            stream=sys.stdout,
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

        logger = logging.getLogger(name)
        return logger
