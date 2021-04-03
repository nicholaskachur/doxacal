"""Logging utilities for doxacal."""

import logging


class SuccintFormatter(logging.Formatter):
    """A formatter which only prints the level name if it's not INFO.

    Based off CC BY-SA 4.0 code by sezanzeb, accessible at
    https://stackoverflow.com/a/62488520
    """

    def format(self, record):
        # pylint: disable=protected-access
        if record.levelno == logging.INFO:
            self._style._fmt = "%(message)s"
        else:
            self._style._fmt = "%(levelname)s %(message)s"
        return super().format(record)


def setup_console_logging(log_level=logging.INFO):
    """Setup logging on the root logger.

    Modules are expected to create their own logger through a getLogger
    call.
    """
    root_logger = logging.getLogger()
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(SuccintFormatter())
    root_logger.setLevel(log_level)
    root_logger.addHandler(console_handler)
