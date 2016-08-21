import requests
import logging
import GenericSensorClass

class WeatherUndergroundSensorClass(GenericSensorClass.GenericSensorClass):

    def __init__(self):

        GenericSensorClass.GenericSensorClass.__init__(self)

        self.data = 0
        self.logging = False

        self.zipcode="16066"
        self.apikey=""


    def GetDataFromSensor(self):

        url = "http://api.wunderground.com:80/api/" + self.apikey + "/conditions/q/" + self.zipcode + ".json"

        if self.logging:
            logging.warning("URL to request weather: "+url)

        r = requests.get(url)

        json_string = r.json()

        self.data = json_string['current_observation']['temp_f']


        if self.logging:
            logging.warning("Returned weather:" + str(self.data))

        return

    def CompareDataFromSensor(self,value):

        if self.logging:
            logging.warning("Comparing "+str(self.data) + " with " + str(value))

        if self.data < value:
            return True
        else:
            return False


