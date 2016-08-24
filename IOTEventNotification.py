#!/usr/bin python
import os
import time
from alerts.spark import SparkRoomAlert
from alerts.local import PrintAlertClass
from sensors.weather import WeatherUndergroundSensor
from sensors.simsensor import SimulatedSensor
from sensors.base import GenericSensorClass
from ConfigParser import SafeConfigParser

"""
MAIN ROUTINE
=====================================================
This is the main routine of the generic event driven
architecture application.

It is a very simple function that uses a time function
to sleep between polling intervals.

#####################################################
"""

# Get hold of the configuration file (package_config.ini)
moduledir = os.path.abspath(os.path.dirname(__file__))
BASEDIR = os.getenv("CAF_APP_PATH", moduledir)

# If we are not running with CAF, use the BASEDIR to get cfg file
tcfg = os.path.join(BASEDIR, "package_config.ini")

CONFIG_FILE = os.getenv("CAF_APP_CONFIG_FILE", tcfg)

cfg = SafeConfigParser()
cfg.read(CONFIG_FILE)

# define the sensor object that will be used to retrieve data from the sensor

# This snippet of code will instantiate the Weather Underground Sensor

#key = cfg.get("wunderground", "api_key")
#zip = cfg.get("wunderground", "zipcode")

#sensor = WeatherUndergroundSensor(key,zip)
#sensor.logging = True


# This snippet of code will instantiate the Simulated Sensor
sensor = SimulatedSensor()
sensor.logging = True

# Define the alerts we want to use

#spark = SparkRoomAlert(cfg)
screen = PrintAlertClass()

# add alerts to sensor
#sensor.add_alert(spark)
sensor.add_alert(screen)

sensor.send_alerts(time.strftime("%b %d %Y, %H:%M:%S ", time.gmtime()) + "IOTEventNotification starting..." )

# Let's loop forever
while True:

    # Let's get data from the sensor
    sensor.read()

    currentdate = time.strftime("%b %d %Y, %H:%M:%S ", time.gmtime())

    """
    Let's compare the data that was retrieved with the
    value to determine the appropriate action
    """
    if sensor.compare(5):

        sensor.send_alerts(currentdate + "ALERT: A new car just appeared at "
                                         "the drive up bank location.   "
                                         "Please Service ASAP!!! " + " (Sensor Hits/Sensor Reads)  ("+
                                          str(sensor.sensorcount)+"/"+ str(sensor.totalcount)+")")
    else:
        sensor.send_alerts(currentdate+"Drive up is currently empty")

    # Sleep for an appropriate time
    time.sleep(10)
