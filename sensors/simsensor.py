import random
import logging
from sensors.base import GenericSensorClass

class SimulatedSensor(GenericSensorClass):

    def __init__(self):

        self.data = 0
#        self.logging = False

        super(SimulatedSensor, self).__init__()


    def read(self):

        # Execute any method in the base class prior to this method
        super(SimulatedSensor,self).read()

        self.data = random.randint(1, 10)

        if self._log:
            logging.warning("Sensor read number: "+ str(self._totalcount) + " Data returned: "+str(self.data))



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