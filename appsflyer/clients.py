import requests
from .specs import APPSFLYER_ENDPOINT
from .exceptions import UnauthorizedDevKeyException
from .events import AppsFlyerEvent

class AppsFlyerClient(object):
    def __init__(self, app_id, dev_key):
        self.dev_key = dev_key
        self.app_id = app_id

    def _prepare_headers(self):
        return {
            'content-type': 'application/json',
            'authentication': self.dev_key
        }

    def _prepare_payload(self, event):
        payload = {'af_events_api': 'true'}
        payload.update(event.to_json())
        return payload

    def interpret_appsflyer_response(self, response):
        if response.status_code == 401:
            raise UnauthorizedDevKeyException()
        print(response.text)
        response.raise_for_status()

    def send_event(self, event):
        assert isinstance(event, AppsFlyerEvent)
        payload = self._prepare_payload(event)
        print(payload)
        appsflyer_endpoint = APPSFLYER_ENDPOINT + self.app_id
        headers = self._prepare_headers()
        response = requests.request("POST", url, headers=headers, json=payload)
        self.interpret_appsflyer_response(response)
