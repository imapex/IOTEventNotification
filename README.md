#IOT Event Notification

This application serves as a generic event notification engine for IOT enabled routers.   The engine will react to any external event and perform some type of notification.

##Examples
* Sending a Spark alert anytime an external temperature sensor hits a certain threshold
* Sending a Tropo notification anytime an external security trigger is tripped

##Main Routine
The core module is in the IOTEventNotification.py.   It implements a infinite loop and performs the folowing:

```{r}
Loop forever
	Get Data from the Sensor 
	Compare Data Received from the Sensor to a value
	If True, alert the user
	Sleep for a period of time
```

##Details of Classes
There are two types of classes that are implemented.   They are a GenericAlertClass and a GenericSensorClass.    These classes represent the base classes to either Alert the users or read data from a sensor.

**GenericAlertClass** - This class implements the generic alerting mechanism.   It provides no function directly, but implements local variables to maintain state.   However, it's purpose is to use it as a foundation for other classes by using inheritance.

The base clase only implements one method:

* **Alert** - This method displays a string

**GenericSensorClass** - This class implements the generic sensor mechanism.  It provides no function directly, but implements local vairables to maintain state.   Similar to the GenericAlertClass, it's purpose is to use it as a foundation for other classes my using inheritance.   

* **read** - This class retrieves data from a sensor.   The data returned from the sensor should be stored in the data variable within theclass so that it can be used for other methods
* **compare(value)** - This class compares the data that was received from the sensor to the value paramter.   It will return a boolean value.

##Code modules provided

* **PrintAlertClass** - This AlertClass will print the data to the screen
* **SparkRoomAlertClass** - This AlertClass will print the data a Cisco Spark Room.  
* **TropoAlertClass** - This AlertClass will print the data to a tropo API to send data to an SMS address.   NOTE:   This requires configuration within Tropo.   Please refer to the [tropo.md] (tropo.md) document
* **SimulatedSensor** - This SensorClass will implement a basic sensor simulation using a random number generator.   
* **WeatherUndergroundSensor** - This SensorClass will receive data from the weather underground API





##Example Usage
All functions of the application is controlled by the configuration file.   This file is called: package_config.ini.  It contains sections for each module with the Notification Engine:

###General Appllication###
In the general application section, we define the paramters for the overall application.

Section Name: application

* delay - The delay time between each reads of the sensor
* success_string - String to be displayed when the sensor read was successful (result of the sensor read **did** meet the pattern)
* failure_string - String to be displayed when the sensor read was not successful (result of the sensor read **did not** meet the pattern)

###Sensors###
With the sensor configurations, you can only have a single sensor.   Therefore, if you enabled multiple sensors, only one will be enabled.

####SimlulatedSensor####
Section name: simulatedsensor

Options:

* enabled - Enable this sensor
* logging - Enable logging of the sensor for debugging mode
* compare_data - Data to compare the returned sensor data to

#### WeatherUndergroundSensor####
Section name: wunderground

Options:

* enabled - Enable this sensor
* logging - Enable logging
* api_key - api_key from Weather Underground to make the
* zipcode - Zip Code to get the weather
* compare_data - Data to compare the returned weather temperature from


###Alerts###
The IOTEventNotification.py provides the cababilities to enable multiple alerts.   Therefore, anytime that the multiple alerts are enabled, it will simultaneously send data to all the enabled sensors at the same time.

####PrintAlertClass####
Section name: print

* enabled - Enable this alert
* logging - Enable logging

####SparkRoomAlertClass####
Section name: spark

* enabled - Enable this alert
* logging - Enable logging
* url - This is the url for the Spark API (Normally, this should not be changed)
* token - This is the spark token that will be used to send the alert
* room_id - This is the id of the room that the alert should be sent to.

####TropoAlertClass####
Section name: tropo

* enabled - Enable this alert
* logging - Enable logging
* token - This is the tropo token that will be used to send the alert to Tropo
* phonenumber - This represents a comma deliminated list of phone numbers to be used for sending the alerts.

