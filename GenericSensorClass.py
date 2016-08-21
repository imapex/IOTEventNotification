#
# This class implements a very simple sensor mechanism
#
# By default, this class create a random number between one and 10.   To simulate a sensor triggering or not.
#
# Alert - This method will display the data in the appropriate format
#
# This generic sensor class can be used as the basis for other more complex clases by inheriting from this base class
#

import random
import logging


class GenericSensorClass():

    def __init__(self):
        self.data = 0
        self.logging = False


    #
    # This method generates a random number and stores that random number in the data variable.
    #
    def GetDataFromSensor(self):


        self.data = random.randint(1, 10)

        if self.logging:
            logging.warning("Generated a number:" + str(self.data))

        return

    #
    #
    # This method will compare the retrieved sensor data with the value.   If the value is less that data
    #  then this data returns true otherwise will be false.
    #
    # This is a very simplistic example of a function that can simulate a sensor.
    #
    def CompareDataFromSensor(self,value):

        if self.logging:
            logging.warning("Comparing "+str(self.data) + " with " + str(value))

        if self.data < value:
            return True
        else:
            return False