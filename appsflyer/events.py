import json

class AppsFlyerEvent(object):
    def __init__(self, appsflyer_id, name, payload, customer_user_id=None, ip=None, time=None, currency=None):
        self.appsflyer_id = appsflyer_id
        self.name = name
        self.payload = json.dumps(payload)
        self.customer_user_id = customer_user_id
        self.ip = ip
        self.time = time
        self.currency = currency

    def to_json(self):
        event_json = {
            'appsflyer_id': self.appsflyer_id,
            'eventName': self.name,
            'eventValue': self.payload or ""
        }
        if self.customer_user_id:
            event_json['customer_user_id'] = self.customer_user_id
        if self.ip:
            event_json['ip'] = self.ip
        if self.currency:
            event_json['eventCurrency'] = self.currency
        if self.time:
            event_json['eventTime'] = self.time
        return event_json

class IosAppsFlyerEvent(AppsFlyerEvent):
    def __init__(self, appsflyer_id, name, payload, idfa=None, customer_user_id=None, ip=None, time=None, currency=None):
        super(IosAppsFlyerEvent, self).__init__(appsflyer_id, name, payload, time=time, currency=currency)
        self.idfa = idfa

    def to_json(self):
        event_json = super(IosAppsFlyerEvent, self).to_json()
        if self.idfa:
            event_json['idfa'] = self.idfa
        return event_json

class AndroidAppsFlyerEvent(AppsFlyerEvent):
    def __init__(self, appsflyer_id, name, payload, advertising_id=None, customer_user_id=None, ip=None, time=None, currency=None):
        super(AndroidAppsFlyerEvent, self).__init__(appsflyer_id, name, payload, time=time, currency=currency)
        self.advertising_id = advertising_id

    def to_json(self):
        event_json = super(AndroidAppsFlyerEvent, self).to_json()
        if self.advertising_id:
            event_json['advertising_id'] = self.advertising_id
        return event_json
