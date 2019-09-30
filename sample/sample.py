import os
from yahoooauth.yoauth import YahooOAuth
from yahoooauth.yfantasy import YahooFantasy
import yahoooauth.resource.game as gameresource

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
token = oauth.credentials['access_token']
yf = YahooFantasy(token)

data = yf.fetch_game_resource(gameresource.YFANTASY_GAME_METADATA.format('223'))
print(data)