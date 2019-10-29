import requests
from .specs import APPSFLYER_ENDPOINT
from .exceptions import UnauthorizedDevKeyException
from .events import IosAppsFlyerEvent, AndroidAppsFlyerEvent

class AppsFlyerClient(object):
    PREFIX_EVENT_CLASS_MAPPING = {
        'id': IosAppsFlyerEvent,
        'com': AndroidAppsFlyerEvent
    }

    def __init__(self, app_id, dev_key):
        self.dev_key = dev_key
        assert isinstance(app_id, str)
        self.event_class = self.get_event_class(app_id)
        self.app_id = app_id
        self.dev_key = dev_key

    def get_event_class(self, app_id):
        result = None
        for prefix, event_class in self.PREFIX_EVENT_CLASS_MAPPING.items():
            if app_id.startswith(prefix):
                result = event_class
        assert result is not None
        return result

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
        assert isinstance(event, self.event_class)
        payload = self._prepare_payload(event)
        appsflyer_endpoint = APPSFLYER_ENDPOINT + self.app_id
        headers = self._prepare_headers()
        response = requests.post(url=appsflyer_endpoint, data=payload, headers=headers)
        self.interpret_appsflyer_response(response)
