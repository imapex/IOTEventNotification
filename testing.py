import unittest
from alerts.spark import SparkRoomAlert
from sensors.weather import WeatherUndergroundSensor


class AlertTestCase(unittest.TestCase):

    def test_create_spark_room_alert(self):
        cfg = {}
        obj = SparkRoomAlert(cfg)
        self.assertIsInstance(obj, SparkRoomAlert)


class SensorTestCase(unittest.TestCase):

    def test_create_weather_sensor(self):
        obj = WeatherUndergroundSensor('foo')
        self.assertIsInstance(obj, WeatherUndergroundSensor)


if __name__ == '__name__':

    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AlertTestCase))
    tests.addTest(unittest.makeSuite(SensorTestCase))

    unittest.main(defaultTest='main')
