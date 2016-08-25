import random
import logging
from sensors.base import GenericSensorClass

class SimulatedSensor(GenericSensorClass):

    def __init__(self):

        self.data = 0

        super(SimulatedSensor, self).__init__()


    def read(self):
        """
        read - This method will read data from the sensor
        :return: nothing
        """
        # Execute any method in the base class prior to this method
        super(SimulatedSensor,self).read()

        # Generate the Random Number to simulate a sensor
        self.data = random.randint(1, 10)

        if self._log:
            logging.warning("Sensor read #"+ str(self._totalcount) + ", Data returned: "+str(self.data))

        return

    def compare(self, value):
        """
        This method will compare the retrieved sensor data with the value.
        If the value is less that data then this data returns true otherwise
        will be false.

        :param value: int value to compare against
        :return: bool result of comparison
        """

        if self._log:
            logging.warning("Comparing {} with {}".format(self.data, value))

        if self.data < value:
            self._sensorcount += 1
            return True
        else:
            return False