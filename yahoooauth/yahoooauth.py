import datetime
import json
import requests
import webbrowser

import yahoooauth.common.credentials as constant

class YahooOAuth:
    AUTH_URL = 'https://api.login.yahoo.com/oauth2/request_auth?client_id={0}&redirect_uri=oob&response_type=code&language=en-us'
    TOKEN_URL = 'https://api.login.yahoo.com/oauth2/get_token'

    def __init__(self, credentials_file: str):
        """ 
        Constructor.
        
        :param credentials_file: The full path of the json file containing client credentials.
        """
        self.credentials_file = credentials_file
        with open(self.credentials_file) as json_file:
            self.credentials = json.load(json_file)
    
    def get_auth_code(self):
        """ 
        Gets authorization code from API. 
        Requires user to login to Yahoo account, allow access and enter auth code.

        :raises exception: If a valid client id is not available.
        """
        if not self.credentials[constant.CLIENT_ID]:
            raise Exception('A valid client id is required to get the authorization code.')

        auth_url = self.AUTH_URL.format(self.credentials[constant.CLIENT_ID])
        webbrowser.open(auth_url)
        self.credentials[constant.AUTHORIZATION_CODE] = input('Enter authorization code: ')
        with open(self.credentials_file, 'w') as credentials_file:
            json.dump(self.credentials, credentials_file, indent=4)
    
    def load_token_response(self, text : str):
        """
        Loads access token response from Yahoo.

        :param text: The server response text.
        :type text: str
        """
        data = json.loads(text)
        self.credentials = {**self.credentials, **data}
        self.credentials[constant.DATE_OBTAINED] = str(int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds()))
        with open(self.credentials_file, 'w') as token_file:
            json.dump(self.credentials, token_file, indent=4)

    def fetch_access_token(self):
        """
        Fetch the access token using the stored authorization code.

        :raises exception: If a valid authorization code is not available
        """
        if not self.credentials[constant.AUTHORIZATION_CODE]:
            raise Exception('A valid authorization code is required to get the access token.')

        response = requests.post(self.TOKEN_URL,
            data = {
                'grant_type':'authorization_code',
                'code':self.credentials[constant.AUTHORIZATION_CODE],
                'redirect_uri':'oob',
                'client_id':self.credentials[constant.CLIENT_ID],
                'client_secret':self.credentials[constant.CLIENT_SECRET]
            })
        if response.status_code == 200:
            self.load_token_response(response.text)
        else:
            message = json.loads(response.text)
            raise Exception("ERROR: {0} - Description: {1}".format(message['error'],message['error_description']))

    def is_token_expired(self):
        """
        Checks whether the access token has expired or not.

        :returns: Whether or not the stored access token has expired.
        """
        now_in_seconds = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
        time_remaining = (now_in_seconds - int(self.credentials[constant.DATE_OBTAINED]))
        if time_remaining > self.credentials[constant.EXPIRES_IN]:
            return True
        else:
            return False

    def refresh_access_token(self):
        """
        Refresh the access token using the stored refresh token.

        :raises exception: If the refresh token is not available.
        """
        if not self.credentials[constant.REFRESH_TOKEN]:
            raise Exception('A valid refresh token is required to refresh the access token.')

        response = requests.post(self.TOKEN_URL,
            data = {
                'client_id':self.credentials[constant.CLIENT_ID],
                'client_secret':self.credentials[constant.CLIENT_SECRET],
                'redirect_uri':'oob',
                'refresh_token':self.credentials[constant.REFRESH_TOKEN],
                'grant_type':'refresh_token'
            })
        if response.status_code == 200:
            self.load_token_response(response.text)
        else:
            message = json.loads(response.text)
            raise Exception("ERROR: {0} - Description: {1}".format(message['error'],message['error_description']))