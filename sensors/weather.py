import logging
import requests
from sensors.base import GenericSensorClass


class WeatherUndergroundSensor(GenericSensorClass):

    def __init__(self, api_key, zip):

        self.data = 0
        self.logging = False

        self.zipcode = zip
        self.apikey = api_key
        super(WeatherUndergroundSensor, self).__init__()

    def read(self):

        self.totalcount += 1

        base_url = "http://api.wunderground.com:80/api/{}".format(self.apikey)
        endpoint = "/conditions/q/{}.json".format(self.zipcode)

        url = base_url + endpoint

        if self.logging:
            logging.warning("URL to request weather: " + url)

        r = requests.get(url)
        json_string = r.json()

        self.data = json_string['current_observation']['temp_f']

        if self.logging:
            logging.warning("Returned weather:" + str(self.data))

        return self.data

    def compare(self, value):
        """
        This method will compare the retrieved sensor data with the value.
        If the value is less that data then this data returns true otherwise
        will be false.

        :param value: int value to compare against
        :return: bool result of comparison
        """

        if self.logging:
            logging.warning("Comparing {} with {}".format(self.data, value))

        if self.data < value:
            self.sensorcount += 1
            return True
        else:
            return False
