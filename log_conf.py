"""
This Code provides the logging mechanisms for our application.  It provides a singleton that will be used by all
functions within our software.
"""

import logging
import logging.handlers
import logging.config

def singleton(cls):
    """
    This singleton function prevents the user from instantiating multiple instances of this class.
    This we only want one logging instance ever.
    :param cls: This is the instance of the class
    :return:
    """
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance()


@singleton
class LoggerManager():
    """
    This Logger Manager Class is really only an init class to set up logging
    """
    def __init__(self):

        # Setup logging mechanisms for both a log file and the screen.

        self.logger = logging.getLogger("IOTEventNotification")
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(module)s/%(funcName)s - %(levelname)s - %(message)s')
        # Start with a Rotating File Handler

        fh = logging.handlers.RotatingFileHandler("IOTEventNotification.log", maxBytes=50000, backupCount=3)
        fh.setFormatter(formatter)

        # Set up a screen handler as well.
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

