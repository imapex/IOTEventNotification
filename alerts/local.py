import logging
from alerts.base import GenericAlertClass


class PrintAlertClass(GenericAlertClass):
    """
    prints alertdata to stdout

    """
    def __init__(self):

        super(PrintAlertClass, self).__init__()

        if self.logging:
            logging.warning("DEBUG: Constructor for PrintAlertClass")

    def trigger(self, alertdata):
        # Alert Method will print the data onto the screen

        print alertdata
