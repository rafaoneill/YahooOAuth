import os
from yahoooauth.yahoooauth import YahooOAuth

# Load credentials file
path = os.path.dirname(os.path.realpath(__file__))
credentials = os.path.join(path, 'credentials.json')
oauth = YahooOAuth(credentials)

# Obtain access token if not available
if oauth.credentials['access_token']:
    oauth.get_auth_code()
    oauth.fetch_access_token()
else:
    if oauth.is_token_expired():
        oauth.refresh_access_token()

print(oauth.credentials['access_token'])