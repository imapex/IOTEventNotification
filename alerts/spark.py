import json
import logging
import requests
from alerts.base import GenericAlertClass


class SparkRoomAlert(GenericAlertClass):
    """
    Sends alerts to a Cisco Spark Room
    """

    def __init__(self, cfg):
        """
        Constructor method when the object is initialized

        :param cfg: Specifies the configuration file that will be used to process the data
        :return: nothing
        """
        self.cfg = cfg
        self.sparkToken = cfg.get("spark", "token")
        self.roomId = cfg.get("spark", "room_id")

        # Call the base class initializer
        super(SparkRoomAlert, self).__init__()

    def post_message(self, text):
        """
        post_message - Internal function used to create the REST API Call and send to the Spark API

        :param text - Message to be posted on the API
        :return message_dict - A Dictionary used to represent the result of the WebAPI Call
        """
        apistring = "https://api.ciscospark.com/v1/messages"

        # Set up the Headers based upon the Tropo API
        headers = {'Authorization': 'Bearer {}'.format(self.sparkToken),
                   'content-type': 'application/json'}

        # Create the payload value that includes the paramters that we need to pass to the Tropo API

        payload = {'roomId': self.roomId, 'text': text}

        if self.log:
            logging.warning("API Call to: " + apistring)
            logging.warning("   Headers: "+ str(headers))
            logging.warning("   Payload: "+ str(payload))

        # Post the API call to the tropo API using the payload and headers defined above
        resp = requests.post(apistring,
                             json=payload, headers=headers)

        message_dict = json.loads(resp.text)
        message_dict['statuscode'] = str(resp.status_code)

        if self.log:
            logging.warning("requests Return Status Code: "+str(resp.status_code))

        return message_dict

    def trigger(self, alertdata):
        """
        trigger - This method will be used to send the message

        :param alertdata: defines the message to be displayed
        :return: returns the dictionary from the resultant display
        """
        return self.post_message(alertdata)
