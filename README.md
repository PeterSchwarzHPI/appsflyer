# AppsFlyer

AppsFlyer client for Python to enable:

- sending server-to-server events to AppsFlyer.

## Installation

```bash
$ pip install git+https://github.com/PeterSchwarzHPI/appsflyer.git
```

## Sending server-to-server iOS Events

```python
from appsflyer.events import IosAppsFlyerEvent
from appsflyer.clients import AppsFlyerClient

appsflyer_id = 'id123456789' # The appsflyer_id for iOS starts with 'id'!
event_name = 'revenue'
event_data = {
    'revenue': 6,
    'quantity': 2
}

# kwargs:
# 'idfa'   - If you wish to map your in-app events from organic users with external partners.
# 'customer_user_id' - Adds a custom user id to the AppsFlyer data sets.
# 'ip'               - Adds the user's ip address to the AppsFlyer data sets.
# 'time'             - If you want to add a specific event time - format: "YYYY-MM-DD HH:MM:SS.MS"
# 'currency'         - If you want to add a specific event currency.
appsflyer_event = IosAppsFlyerEvent(appsflyer_id, event_name, event_data, **kwargs) 
appsflyer_client = AppsFlyerClient('DEV_KEY', 'APP_ID')
appsflyer_client.send_event(event)

```

## Sending server-to-server Android Events

```python
from appsflyer.events import AndroidAppsFlyerEvent
from appsflyer.clients import AppsFlyerClient

appsflyer_id = 'com.appsflyer.appname' # The appsflyer_id for Android starts with 'com.appsflyer'!
event_name = 'revenue'
event_data = {
    'revenue': 6,
    'quantity': 2
}

# kwargs:
# 'advertising_id'   - If you wish to map your in-app events from organic users with external partners.
# 'customer_user_id' - Adds a custom user id to the AppsFlyer data sets.
# 'ip'               - Adds the user's ip address to the AppsFlyer data sets.
# 'time'             - If you want to add a specific event time - format: "YYYY-MM-DD HH:MM:SS.MS"
# 'currency'         - If you want to add a specific event currency.
appsflyer_event = AndroidAppsFlyerEvent(appsflyer_id, event_name, event_data, **kwargs)
appsflyer_client = AppsFlyerClient('DEV_KEY', 'APP_ID')
appsflyer_client.send_event(event)

```

## License

GNU General Public License v3.0

## Author

[PeteBlack](https://github.com/PeterSchwarzHPI)
