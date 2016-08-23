#
# This class implements a very simple sensor mechanism
#
#
# This generic sensor class can be used as the basis for
# other more complex clases by inheriting from this base class
#


class GenericSensorClass(object):

    def __init__(self):
        self.data = 0
        self.logging = False
        self.alerts = list()

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

        pass

    def compare(self, value):
        # will be overridden by child
        pass

    def send_alerts(self, alertdata):
        response = dict()
        for a in self.alerts:
            response[a] = a.trigger(alertdata)
        return response
