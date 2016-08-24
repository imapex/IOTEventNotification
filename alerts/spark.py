import json
import logging
import requests
from alerts.base import GenericAlertClass


class SparkRoomAlert(GenericAlertClass):
    """
    Sends alerts to a Cisco Spark Room
    """

    def __init__(self, cfg):

        self.cfg = cfg
        self.sparkToken = cfg.get("spark", "token")
        self.roomId = cfg.get("spark", "room_id")
        super(SparkRoomAlert, self).__init__()
        if self.log:
            logging.warning("DEBUG: Constructor for PrintAlertClass")

    def post_message(self, text, toPersonId='', toPersonEmail=''):
        headers = {'Authorization': 'Bearer {}'.format(self.sparkToken),
                   'content-type': 'application/json'}

        payload = {'roomId': self.roomId, 'text': text}
        if toPersonId:
            payload['toPersonId'] = toPersonId
        if toPersonEmail:
            payload['toPersonEmail'] = toPersonEmail
        resp = requests.post("https://api.ciscospark.com/v1/messages",
                             json=payload, headers=headers)
        message_dict = json.loads(resp.text)
        message_dict['statuscode'] = str(resp.status_code)
        return message_dict

    def trigger(self, alertdata):
        return self.post_message(alertdata)
