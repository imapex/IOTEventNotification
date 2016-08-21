#IOT Event Notification

This application serves as a generic event notification engine for IOT enabled routers.   The engine will react to any external event and perform some type of notification.

##Examples
* Sending a Spark alert anytime an external temperature sensor hits a certain threshold
* Sending a Tropo notification anytime an external security trigger is tripped

##Main Routine
The IOTeventNotification.py function is the IOTEventRoutine.   Basically, it implements a infinite loop and performs the folowing:

```{r}
Loop forever
	Get Data from the Sensor 
	Compare Data Received from the Sensor to a value
	If True, alert the user
	Sleep for a period of time
```

##Details of Generic Functions
There are two types of classes that are implemented.   They are a GenericAlertClass and a GenericSensorClass.    These classes perform the actual function.

**GenericAlertClass** - This class implements the generic alerting mechanism.   The default it does not, but implements local variables to maintain state.   However, the function of it is to use it as a foundation for other classes by using inheritance.

The base clase only implements one method:

* **Alert** - This method displays a string

**GenericSensorClass** - This class implements the generic sensor mechanism.  The default behavior implements a simulated sensor by using a random number generator.   

* **GetDataFromSensor** - This class retrieves data from a sensor.   The data returned from the sensor should be stored in the data variable within theclass so that it can be used for other methods
* **CompareDataFromSensor(value)** - This class compares the data that was received from the sensor to the value paramter.   It will return a boolean value.

##Code modules provided

* **PrintAlertClass** - This AlertClass will print the data to the screen
* **SparkRoomAlertClass** - This AlertClass will print the data a Cisco Spark Room.   
* **WeatherUndergroundSensorClass** - This SensorClass will receive data from the weather underground API



##Example Usage
To create your own class to inherit from these base classes.   The following example allows you to create your own alerting class

```{r}
import GenericAlertClass
class MyCustomAlertClass(GenericAlertClass.GenericAlertClass):
    def __init__(self):

        GenericAlertClass.GenericAlertClass.__init__(self)
    
    def Alert(self,alertdata)
    
    # Implement Custom Code to Alert the User    
```
