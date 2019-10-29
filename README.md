# AppsFlyer

AppsFlyer client for Python to enable:

- sending server-to-server events to AppsFlyer.

## Installation

```bash
$ pip install git+https://github.com/PeterSchwarzHPI/appsflyer.git
```

## Sending server-to-server RevenuEvents

```python
from appsflyer import AppsFlyerClient, RevenueEvent

appsflyer_id = 'id123456789' # The appsflyer_id for iOS or Android
revenue = 50.69
currency = 'EUR'

# kwargs:
# 'idfa'             - If you wish to map your in-app events from organic users with external partners. -> Ios
# 'advertising_id'   - If you wish to map your in-app events from organic users with external partners. -> Android
# 'customer_user_id' - Adds a custom user id to the AppsFlyer data sets.
# 'ip'               - Adds the user's ip address to the AppsFlyer data sets.
# 'time'             - If you want to add a specific event time - format: "YYYY-MM-DD HH:MM:SS.MS"
appsflyer_event = RevenueEvent(appsflyer_id, revenue, currency, **kwargs) 
appsflyer_client = AppsFlyerClient('DEV_KEY', 'APP_ID')
appsflyer_client.send_event(appsflyer_event)

```

## Sending server-to-server LoginEvents

```python
from appsflyer import AppsFlyerClient, LoginEvent

appsflyer_id = 'id123456789' # The appsflyer_id for iOS or Android

# kwargs:
# 'idfa'             - If you wish to map your in-app events from organic users with external partners. -> Ios
# 'advertising_id'   - If you wish to map your in-app events from organic users with external partners. -> Android
# 'customer_user_id' - Adds a custom user id to the AppsFlyer data sets.
# 'ip'               - Adds the user's ip address to the AppsFlyer data sets.
# 'time'             - If you want to add a specific event time - format: "YYYY-MM-DD HH:MM:SS.MS"
appsflyer_event = LoginEvent(appsflyer_id, **kwargs)
appsflyer_client = AppsFlyerClient('DEV_KEY', 'APP_ID')
appsflyer_client.send_event(appsflyer_event)

```

## License

GNU General Public License v3.0

## Author

[PeteBlack](https://github.com/PeterSchwarzHPI)
