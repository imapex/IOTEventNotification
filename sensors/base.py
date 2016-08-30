#
# This class implements a very simple sensor mechanism
#
# By default this class does nothing, but can be used for future functionality
#
# This generic sensor class can be used as the basis for
# other more complex clases by inheriting from this base class
#


class GenericSensorClass(object):

    def __init__(self):
        self.data = 0

        self._comparedata=0
        self._log = False
        self.alerts = list()

        self._totalcount = 0
        self._sensorcount = 0

    @property
    def log(self):
        return self._log

    @log.setter
    def log(self, value):
        self._log = value

    @property
    def comparedata(self):
        return self._comparedata

    @comparedata.setter
    def comparedata(self, value):
        self._comparedata = int(value)

    @property
    def totalcount(self):
        return self._totalcount

    @totalcount.setter
    def totalcount(self, value):
        self._totalcount = value

    @property
    def sensorcount(self):
        return self._sensorcount

    @sensorcount.setter
    def sensorcount(self, value):
        self._sensorcount = value



    def add_alert(self, alert):
        """
        adds an alert object to the sensor

        :param alert: Alert object instance
        :return:
        """
        if isinstance(alert, list):
            self.alerts = self.alerts + alert
        else:
            self.alerts.append(alert)

    def read(self):
        """
        this method should be overriden by child classes
        w/ sensor specific code

        :return:
        """
        self._totalcount += 1

        pass

    def compare(self, value):
        # will be overridden by child
        pass

    def send_alerts(self, alertdata):
        response = dict()
        for a in self.alerts:
            response[a] = a.trigger(alertdata)
        return response
