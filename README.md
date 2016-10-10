#IOT Event Notification

This application serves as a generic event notification engine for IOT enabled routers.   The engine will react to any external event and perform some type of notification.

##Examples
* Sending a Spark alert anytime an external temperature sensor hits a certain threshold
* Sending a Tropo notification anytime an external security trigger is tripped

For more detailed information on the technical details behind the modules, please see [developer.md] (developer.md).    


##Quick Start
To quickly get started with this module, let's configure the application to automatically generate a Spark Notification anytime the weather falls below 50 degrees for zip code 16066.

#####Determine the Spark Room ID to send the alert to#####

1. Go to https://developer.ciscospark.com/# and click on the "Log In Button"
2. Log in using your Spark Credentials
3. Click on the Get Started Button
4. Click on the "Rooms" Link under the "API Reference" on the left side
5. Click on the List Rooms API
6. Click on "Test Mode" to enable Test Mode
7. Click on the Run Button
8. On the Right Hand Side, you will see JSON off all the rooms that you are a member with, Pick one of the rooms and copy the value of "id" for the room that you want to send notifications

#####Determine your Spark Token#####
1. Go to https://developer.ciscospark.com/# and click on the "Log In Button"
2. Log in using your Spark Credentials
3. Click on your picture in the top right hand corner
4. Your Spark Token will be displayed
5. You can Select Copy to copy that Spark ID

#####Register For a Weather Underground#####
1. Go to https://www.wunderground.com/weather/api/
2. Click on Pricing and select the free plan and click on the "Purchase Key" button
3. Once you have created an account, you can log in and click on "Key Settings"
4. Under the field "Key ID", you will find your Weather Underground API Key.

#####Setup Application#####
1. Download all the files from the github repository to your computer
2. Copy the package_config.ini.sample to package_config.ini
3. Edit the "package_config.ini" file using your favorite editor
4. Under the application section, set the log\_level to be 10 for debug purposes
5. Under the application section, set the delay value to 20.   This represents that we will check the sensor every 10 seconds
6. Under the application section, set the operator value to be <.   This represents that we want to check to see if the sensor is less than a appropriate value.
7. Under the print section, set enabled to True.   This will display that data to the screen.
8. Under the spark section, set enabled to True.   This will active the spark alerting mechanism.
9. Under the spark section, set the token to be the token value that you obtained from the developer.ciscospark.com website
10. Under the spark section, set the room\_id to match the spark room ID that you obtained from the developer.ciscospark.com website to represent the room that you will be writing alerts to.
11. Under the wunderground section, set enabled to True
12. Under the wunderground section, set api\_key to match the api key that you created on the Weather Underground Website
13. Under the wunderground section, set zipcode to be 16066 (Or any zip code that you want to find the weather for.
14. Under the wunderground section, set compare\_date to 50.
15. Run the application by using the following:

```
python IOTEventNotification.py
``` 

If everthing worked out correctly you should now see the application starting up and get data from the sensors, compare the data and then display the message.





