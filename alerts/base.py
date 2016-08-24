#
# This class implements a very simple alerting object
#
# By default, this class will do nothing.
#
# This generic alert class must be used as the base class to inherit from
#
import logging


class GenericAlertClass(object):

    def __init__(self):
        self._log = False

        if self.log:
            logging.warning("DEBUG: Constructor for GenericAlertClass")

    # Alert Method will print the data onto the screen
    def Alert(self, alertdata):
        pass

    # Getter to return the log value
    @property
    def log(self):
        return self._log

    # Setter to set the log value
    @log.setter
    def log(self, value):
        self._log = value