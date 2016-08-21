#
# This class implements a very print to the screen alerting function
#
# Alert - This method will display the data in the appropriate format
#
# This generic alert class can be used as the basis for other more complex clases
#

import GenericAlertClass

class PrintAlertClass(GenericAlertClass.GenericAlertClass):

    def __init__(self):

        GenericAlertClass.GenericAlertClass.__init__(self)

        if self.logging:
            logging.warning("DEBUG: Constructor for PrintAlertClass")


    # Alert Method will print the data onto the screen
    def Alert(self,alertdata):
        print alertdata