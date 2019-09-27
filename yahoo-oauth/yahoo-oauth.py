import json
import requests

class YahooOAuth:
    def __init__(self, credentials: str):
        """
        Parameters
        ----------
        credentials : str
            The name of the json file containing client credentials.
        """
        data = json.loads(credentials)
        self.client_id = data['client_id']
        self.client_secret = data['client_secret']
        self.auth_code = data['auth_code']