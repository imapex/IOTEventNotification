#!/usr/bin python
import time
#import PrintAlertClass
#import GenericSensorClass
import SparkRoomAlertClass
import WeatherUndergroundSensorClass

#####################################################
#
# MAIN ROUTINE
#
# This is the main routine of the generic event driven architecture application
#
# The function takes two classes that will define the input (Sensor) and the output(Alert)
#
# It is a very simple function that uses a time function to sleep between polling intervals.
#
#####################################################


# This defines the alert object that will be used to notify the user
#AlertUser = PrintAlertClass.PrintAlertClass()
AlertUser =  SparkRoomAlertClass.SparkRoomAlertClass()

# This defines the sensor object that will be used to retrieve data from the sensor
#Sensor = GenericSensorClass.GenericSensorClass()
Sensor = WeatherUndergroundSensorClass.WeatherUndergroundSensorClass()
Sensor.logging=True

# Let's loop forever
while True:

    # Let's get data from the sensor
    Sensor.GetDataFromSensor()

    currentdate = time.strftime("%b %d %Y, %H:%M:%S ", time.gmtime())

    # Let's compare the data that was retrieved with the value to determine the appropriate action

    if Sensor.CompareDataFromSensor(100) :

        AlertUser.Alert(currentdate + "ALERT: A new car just appeared at the drive up bank location.   Please Service ASAP")
    else:
        AlertUser.Alert(currentdate+"Drive up is currently empty")

    # Sleep for an appropriate time
    time.sleep(10)







