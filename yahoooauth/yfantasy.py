import requests

class YahooFantasy:
    API_URL='https://fantasysports.yahooapis.com{0}?format=json'

    def __init__(self, token: str):
        """
        Constructor.

        :param token: The token to use for each api request.
        """
        self.headers = {
            'Authorization':'Bearer ' + token
        }

    def fetch_game_resource(self, endpoint: str):
        url = self.API_URL.format(endpoint)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception()