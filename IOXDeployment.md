#IOT Event Notification 
##Deployment for Cisco IOx Devices

The IOT Event Notification Application can be deployed on Cisco IOx Devices.  A certain class of Cisco routers can support running applications on the platform.   These devices can be identified by looking at the developer guide for IOx devices.   This developer guide can be found at the following location:  [https://developer.cisco.com/site/iox/docs/#introduction-to-iox] (https://developer.cisco.com/site/iox/docs/#introduction-to-iox)

##High Level Deployment Steps

1. Download the ioxclient in the IOx Developers Kit
2. Configure the router as per the instructions in the developer kit
3. Set default values for the ioxclient
4. Build the application using ioxclient to package it
5. Deploy the applicaiton to the router using either ioxclient or manually via the web browser.

##ioxclient
The IOx developers kit leverages the ioxclient application.    This application is used to create the deployment file for the application that can be deployed on the Cisco router.   The ioxclient can also be used to automatically connect to the router, deploy the application and start it.   However, in this example, we are deploying the application manually instead.

When you run the application for the first time, ioxclient will attempt to set the default variables.   It will create a file called .ioxclientcfg.yaml in the HOME directory of the user that is running the application.   In the example below, we are basically selecting all the default values which will work for our application.

```
CBOGDON-M-D1FU:IOTEventNotification cbogdon$ ./ioxclient
Config file not found :  /Users/cbogdon/.ioxclientcfg.yaml
Creating one time configuration..
Your / your organization's name : Cisco
Your / your organization's URL : www.cisco.com
Your IOx platform's IP address[127.0.0.1] : 
Your IOx platform's port number[8443] : 
Authorized user name[root] : 
Password for root : 
Local repository path on IOx platform[/software/downloads]: 
URL Scheme (http/https) [https]: 
API Prefix[/iox/api/v2/hosting/]: 
Your IOx platform's SSH Port[2222]: 
Your RSA key, for signing packages, in PEM format[]: 
Your x.509 certificate in PEM format[]: 
Activating Profile  default
Saving current configuration
```

Once you have set the configurations for the first time, you can then package the application by using the following command:

```
./ioxclient package .
```

Sample output is provided below.

```
CBOGDON-M-D1FU:IOTEventNotification cbogdon$ ./ioxclient package .
Currently active profile :  default
Command Name:  package
No rsa key and/or certificate files to sign the package
Checking if package descriptor file is present..
Validating descriptor file /Users/cbogdon/coding/IOTEventNotification/package.yaml with package schema definitions
Parsing descriptor file..
Found schema version  2.0
Loading schema file for version  2.0
Validating package descriptor file..
File /Users/cbogdon/coding/IOTEventNotification/package.yaml is valid under schema version 2.0
Created Staging directory at :  /var/folders/1q/ks61mr056rd2y62zzvs0zdm40000gn/T/291237708
Copying contents to staging directory
Checking for application runtime type
Detected Python application. Attempting to install dependencies present in requirements.txt ..
Error installing app dependencies. Is 'pip' not installed? 
Creating an inner envelope for application artifacts
Excluding  .idea/IOTEventNotification.iml
Excluding  .idea/misc.xml
Excluding  .idea/modules.xml
Excluding  .idea/vcs.xml
Excluding  .idea/workspace.xml
Excluding  package.tar
Generated  /var/folders/1q/ks61mr056rd2y62zzvs0zdm40000gn/T/291237708/artifacts.tar.gz
Calculating SHA1 checksum for package contents..
Package MetaData file was not found at  /private/var/folders/1q/ks61mr056rd2y62zzvs0zdm40000gn/T/291237708/.package.metadata
Wrote package metadata file :  /private/var/folders/1q/ks61mr056rd2y62zzvs0zdm40000gn/T/291237708/.package.metadata
Root Directory :  /private/var/folders/1q/ks61mr056rd2y62zzvs0zdm40000gn/T/291237708
Output file:  /var/folders/1q/ks61mr056rd2y62zzvs0zdm40000gn/T/501113403
Path:  .package.metadata
SHA1 : 708ad888990c8a7626099e5924760721ba9d58fa
Path:  artifacts.tar.gz
SHA1 : a3c79df960acb0f3f78ddaa76cc1563721f42904
Path:  package.yaml
SHA1 : ec20c7736848daf29831890fba066d4d343443f2
Path:  package_config.ini
SHA1 : 1f10e522a295996963668be42dc62d0c3ce6cd36
Generated package manifest at  package.mf
Generating IOx Package..
Package generated at /Users/cbogdon/coding/IOTEventNotification/package.tar
CBOGDON-M-D1FU:IOTEventNotification cbogdon$ 
```
ioxclient now successfully package the .tar file that can now be used to deploy to the IOx router.  NOTE: ioxclient will also automatically package the packkage_config.ini into the archive which will be used for configurations.

## Connecting to IOx Local Manager to install applications

If you have set up the router successfully for IOx applications as per the developers kit, you should be able to open a web browser and enter https://{router ip}:8443 in the address bar.   This will bring up the Cisco IOx Local Manager gui which you can now log in using router credentials.


1. In the Cisco IOx Local Manager Applications tab, click Add New. The Deploy application dialog box appear.
2. In the Deploy Application dialog box, take these actions:
    * In the Application ID field, enter iotnotify.
    * In the Select Application Archive field, click Choose File and navigate to and select the sample application file that you created using **ioxnotify**.
    * Click OK.
3. The application file uploads to Cisco IOx.
    * When you see the pop-up message “Successfully Deployed,” click OK.
    * The Cisco IOx Local Manager Applications tab updates to show the **ioxnotify** area.
4. In the **ioxnotify** area, click the Activate button.
    * The Applications > Resources tab displays.
5. In the Network Configuration area of the Applications > Resources tab, take these actions:
    * Choose iox-nat0 Default Network – nat from the eth0 drop-down list.
6. In the Applications > Resources tab, click the Activate button to activate the application.
7. Click the Applications tab.
    * In the **ioxnotify** area, click the Start button.

The application should now be running on the router.