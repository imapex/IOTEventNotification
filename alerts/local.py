import logging
from alerts.base import GenericAlertClass


class PrintAlertClass(GenericAlertClass):
    """
    prints alertdata to stdout

    """
    def __init__(self):
        """
        Constructor method when the object is initialized

        """
        # Call the base class initializer
        super(PrintAlertClass, self).__init__()


    def trigger(self, alertdata):
        """
        trigger - This method will be used to send the message

        :param alertdata: defines the message to be displayed
        :return: nothing
        """

        print alertdata
