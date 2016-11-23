import random
from log_conf import LoggerManager
import operator
from sensors.base import GenericSensorClass

class SimulatedSensor(GenericSensorClass):

    def __init__(self):

        super(SimulatedSensor, self).__init__()

        self.data = 0



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
           LoggerManager.logger.debug("Sensor read #"+ str(self._totalcount) + ", Data returned: "+str(self.data))

        return

    def compare(self, value, op_type):
        """
        This method will compare the retrieved sensor data with the value.
        If the value is less that data then this data returns true otherwise
        will be false.

        :param value: int value to compare against
               op_type: type of operator used to compare the values
        :return: bool result of comparison
        """
        ops = {'>': operator.gt,
               '<': operator.lt,
               '>=': operator.ge,
               '<=': operator.le,
               '=': operator.eq}

        if self._log:
            LoggerManager.logger.debug("Comparing {} with {} using operator '{}'".format(self.data, value, op_type))

        if ops[op_type](self.data,value) :
            self._sensorcount += 1
            return True
        else:
            return False