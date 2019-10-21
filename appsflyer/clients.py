import requests
from .specs import APPSFLYER_ENDPOINT
from .exceptions import UnauthorizedDevKeyException
from .events import IosAppsFlyerEvent, AndroidAppsFlyerEvent

class AppsFlyerClient(object):
    def __init__(self, dev_key):
        self.dev_key = dev_key

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
        response.raise_for_status()

    def send_event(self, event):
        assert isinstance(event, IosAppsFlyerEvent) or isinstance(event, AndroidAppsFlyerEvent)
        payload = self._prepare_payload(event)
        appsflyer_endpoint = APPSFLYER_ENDPOINT + event.app_id
        headers = self._prepare_headers()
        response = requests.post(url=appsflyer_endpoint, data=payload, headers=headers)
        self.interpret_appsflyer_response(response)
