# YahooOAuth
Python module to consume Yahoo Fantasy API

## Compiling and installing package from source
```shell
python3 setup.py bdist_wheel
python3 -m pip install dist/yahoooauth-1.0-py3-none-any.whl --force --user
```

## Usage
```python
import os
from yahoooauth.yoauth import YahooOAuth

# Load credentials file
path = os.path.dirname(os.path.realpath(__file__))
credentials = os.path.join(path, 'credentials.json')
oauth = YahooOAuth(credentials)

# Obtain access token if not available
if not oauth.credentials['access_token']:
    oauth.get_auth_code()
    oauth.fetch_access_token()
else:
    if oauth.is_token_expired():
        oauth.refresh_access_token()

print(oauth.credentials['access_token'])
```