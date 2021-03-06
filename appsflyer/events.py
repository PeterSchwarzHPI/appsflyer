import json

class AppsFlyerEvent(object):
    def __init__(self, appsflyer_id, name, payload=None, idfa=None, advertising_id=None, customer_user_id=None, ip=None, time=None):
        self.appsflyer_id = appsflyer_id
        self.name = name
        self.payload = payload
        self.idfa = idfa
        self.advertising_id = advertising_id
        self.customer_user_id = customer_user_id
        self.ip = ip
        self.time = time

    def to_json(self):
        event_json = {
            'appsflyer_id': self.appsflyer_id,
            'eventName': self.name,
            'eventValue': json.dumps(self.payload) if self.payload else ""
        }
        if self.customer_user_id:
            event_json['customer_user_id'] = self.customer_user_id
        if self.ip:
            event_json['ip'] = self.ip
        if self.time:
            event_json['eventTime'] = self.time
        if self.idfa:
            event_json['idfa'] = self.idfa
        else:
            event_json['advertising_id'] = self.advertising_id
        return event_json

class RevenueEvent(AppsFlyerEvent):
    def __init__(self, appsflyer_id, revenue, currency, idfa=None, advertising_id=None, customer_user_id=None, ip=None, time=None):
        payload = {'af_revenue': '{}'.format(revenue)}
        super(RevenueEvent, self).__init__(appsflyer_id, 'af_purchase', payload=payload, idfa=idfa, advertising_id=advertising_id, customer_user_id=customer_user_id, ip=ip, time=time) 
        self.currency = currency

    def to_json(self):
        event_json = super(RevenueEvent, self).to_json()
        event_json['eventCurrency'] = self.currency
        return event_json

class LoginEvent(AppsFlyerEvent):
    def __init__(self, appsflyer_id, idfa=None, advertising_id=None, customer_user_id=None, ip=None, time=None):
        super(LoginEvent, self).__init__(appsflyer_id, 'af_login', idfa=idfa, advertising_id=advertising_id, customer_user_id=customer_user_id, ip=ip, time=time)

class RegistrationEvent(AppsFlyerEvent):
    def __init__(self, appsflyer_id, registration_method, idfa=None, advertising_id=None, customer_user_id=None, ip=None, time=None):
        payload = {'af_registration_method': '{}'.format(registration_method)}
        super(RegistrationEvent, self).__init__(appsflyer_id, 'af_complete_registration', payload=payload, idfa=idfa, advertising_id=advertising_id, customer_user_id=customer_user_id, ip=ip, time=time)
