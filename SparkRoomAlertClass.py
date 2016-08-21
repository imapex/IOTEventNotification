#
# This class implements generic display to a Spark room.
#
# Alert - This method will display the data to the appropriate spark room.
#
# You will need to provide both the sparkToken and the Room ID to
#

import requests
import json
import logging

import GenericAlertClass

def _fix_at(at):
    at_prefix = 'Bearer '

    return 'Bearer ' + at



def post_message(at, roomId, text, toPersonId='', toPersonEmail=''):
    headers = {'Authorization': _fix_at(at), 'content-type': 'application/json'}
    payload = {'roomId': roomId, 'text': text}
    if toPersonId:
        payload['toPersonId'] = toPersonId
    if toPersonEmail:
        payload['toPersonEmail'] = toPersonEmail
    resp = requests.post("https://api.ciscospark.com/v1/messages", json=payload, headers=headers)
    message_dict = json.loads(resp.text)
    message_dict['statuscode'] = str(resp.status_code)
    return message_dict

class SparkRoomAlertClass(GenericAlertClass.GenericAlertClass):

    def __init__(self):

        GenericAlertClass.GenericAlertClass.__init__(self)

        self.sparkToken = ""
        self.roomID = ""

        if self.logging:
            logging.warning("DEBUG: Constructor for PrintAlertClass")

    def Alert(self,alertdata):
        post_message(self.sparkToken, self.roomID, alertdata)
