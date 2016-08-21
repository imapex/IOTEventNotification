#
# This class implements a very simple alerting mechanism
#
# By default, this class will display the data on the screen.   However, it can be
# extending and customized to be using any alert mechanism
#
# Alert - This method by default will do nothing.
#
# This generic alert class must be used as the base class to inherit from
#

class GenericAlertClass():

    def __init__(self):
        self.logging = False

        if self.logging:
            logging.warning("DEBUG: Constructor for GenericAlertClass")


    # Alert Method will print the data onto the screen
    def Alert(self,alertdata):
        pass

