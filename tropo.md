#Details for Tropo Alert
This document is meant to describe the prework that will need to be done to enable the Tropo alerts within the IOTEventNotification.

##Step 1 - Sign up for Tropo
To sign up for tropo, you must go to www.tropo.com and get an account.
##Step 2 - Create a new application
1. Log into tropo
2. From the Home page, select: "Applications"
2. Select: "My Apps->Create Application"
3. Enter a name under basic information
4. Select "Scripting API".   For the purposes of this application, we ran the API on Tropo's servers because it is easier.   However, you can always host the script on your own servers.
5. Select "New Script"
6. Enter the following script into the test editor

	```{r}
	call("+1"+numberToDial, {
		   network:"SMS"});
		say(alertMessage);
	```
7. Press the save button
8. 	Associate the script to a phone number byt selecting a new phone number from the list.   If you don't already have a phone number, you should create a new one.
9. Press Create App

##Step 3 - Associate the Script with your application
1. Once your application is created, on the bottom of the page in the API Keys section, there will be a "messaging" key.   Copy this key.
2. Within the configuration file of the IOTEventNotification.py application, enter this key in the configuration field under the "tropo" section