#!/usr/bin python
import os
import time
#import logging
#import logging.handlers
from alerts.spark import SparkRoomAlert
from alerts.local import PrintAlertClass
from sensors.weather import WeatherUndergroundSensor
from sensors.simsensor import SimulatedSensor
from sensors.base import GenericSensorClass
from ConfigParser import SafeConfigParser
from alerts.tropo import TropoAlert
from log_conf import LoggerManager

"""
MAIN ROUTINE
=====================================================
This is the main routine of the generic event driven
architecture application.

It is a very simple function that uses a time function
to sleep between polling intervals.

#####################################################
"""

LoggerManager.logger.info("IOT Event Notification Starting....")


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

cancontinue = False
if (cfg.get("wunderground","enabled") == "True"):

    LoggerManager.logger.info("Weatherunderground Sensor Enabled...")
    key = cfg.get("wunderground", "api_key")
    zip = cfg.get("wunderground", "zipcode")
    comparedata = cfg.get("wunderground","compare_data")

    sensor = WeatherUndergroundSensor(key,zip)
    if (cfg.get("wunderground", "logging") == "True"):
        sensor.log = True
    sensor.comparedata = comparedata
    cancontinue = True
elif (cfg.get("simulatedsensor","enabled") == "True"):

    # This snippet of code will instantiate the Simulated Sensor
    LoggerManager.logger.info("Simulated Sensor Enabled...")
    comparedata = cfg.get("simulatedsensor","compare_data")
    sensor = SimulatedSensor()
    if (cfg.get("simulatedsensor", "logging") == "True"):
        sensor.log = True
    sensor.comparedata = int(comparedata)
else:
    LoggerManager.logger.error("ERROR: At least one sensor must be defined. Please enable at least one sensor.")
    exit (-1)

# Define the alerts we want to use

cancontinue = False

# This code will instantiate the Print Alert Class - Check to see if it is enabled
if (cfg.get("print","enabled") == "True"):
    LoggerManager.logger.info("Print Alert Enabled for output...")
    screen = PrintAlertClass()

    if (cfg.get("print","logging") == "True"):
        screen.log = True

    sensor.add_alert(screen)
    cancontinue = True

# This code will instantiate the Tropo Alert Class - Check to see if it is enabled
if (cfg.get("tropo","enabled") == "True"):
    LoggerManager.logger.info("Tropo Alert Enabled for output...")
    tropo = TropoAlert(cfg)

    if (cfg.get("tropo","logging") == "True"):
        tropo.log = True

    sensor.add_alert(tropo)
    cancontinue = True

# This code will instantiate the Tropo Alert Class - Check to see if it is enabled
if (cfg.get("spark","enabled") == "True"):
    LoggerManager.logger.info("Spark Alert Enabled for output...")
    spark = SparkRoomAlert(cfg)

    if (cfg.get("spark","logging") == "True"):
        spark.log = True

    sensor.add_alert(spark)
    cancontinue = True

if not cancontinue:
    LoggerManager.logger.error("ERROR: No alerts are enabled.   Please enable at least one alert.")
    exit(-1)

# Let's loop forever
while True:

    # Let's get data from the sensor
    sensor.read()

    currentdate = time.strftime("%b %d %Y, %H:%M:%S ", time.gmtime())

    """
    Let's compare the data that was retrieved with the
    value to determine the appropriate action
    """

    if sensor.compare(sensor.comparedata):

        sensor.send_alerts(currentdate + "ALERT: A new car just appeared at "
                                         "the drive up bank location.   "
                                         "Please Service ASAP!!! " + " (Sensor Hits/Sensor Reads)  ("+
                                          str(sensor.sensorcount)+"/"+ str(sensor.totalcount)+")")
    else:
        sensor.send_alerts(currentdate + "Drive up is currently empty")

    # Sleep for an appropriate time
    time.sleep(10)
