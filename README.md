# Appsflyer

AppsFlyer client for Python to enable:

- sending events to Appsflyer.

## Installation

```bash
$ pip install git+https://github.com/PeterSchwarzHPI/appsflyer.git
```

## Usage

```python
from appsflyer import AppsFlyerClient

event = {
    'revenue': 6,
    'quantity': 2
}
appsflyer_client = AppsFlyerClient('DEV_KEY', 'APP_ID', advertising_id='ADVERTISING_ID')
appsflyer_cliend.send_event(event)

```

## License

GNU General Public License v3.0

## Author

[PeteBlack](https://github.com/PeterSchwarzHPI)
