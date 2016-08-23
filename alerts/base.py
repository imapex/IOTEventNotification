#
# This class implements a very simple alerting mechanism
#
# By default, this class will display the data on the screen.
# However, it can be extended and customized to be
# using any alert mechanism
#
# This generic alert class must be used as the base class to inherit from
#
import logging


class GenericAlertClass(object):

    def __init__(self):
        self.logging = False

        if self.logging:
            logging.warning("DEBUG: Constructor for GenericAlertClass")

    # Alert Method will print the data onto the screen
    def Alert(self, alertdata):
        pass
