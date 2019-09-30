import datetime
import json
import requests
import webbrowser

import yahoooauth.common.credentials as constant
import yahoooauth.common.messages as messages

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
            raise Exception(messages.INVALID_CLIENT_ID)

        auth_url = self.AUTH_URL.format(self.credentials[constant.CLIENT_ID])
        webbrowser.open(auth_url)
        self.credentials[constant.AUTHORIZATION_CODE] = input(messages.INPUT_AUTHORIZATION_CODE)
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

        :raises exception: If a valid authorization code is not available.
        """
        if not self.credentials[constant.AUTHORIZATION_CODE]:
            raise Exception(messages.INVALID_AUTHORIZATION_CODE)

        response = requests.post(self.TOKEN_URL,
            data = {
                constant.GRANT_TYPE:constant.AUTHORIZATION_CODE,
                constant.CODE:self.credentials[constant.AUTHORIZATION_CODE],
                constant.REDIRECT_URI:'oob',
                constant.CLIENT_ID:self.credentials[constant.CLIENT_ID],
                constant.CLIENT_SECRET:self.credentials[constant.CLIENT_SECRET]
            })
        if response.status_code == 200:
            self.load_token_response(response.text)
        else:
            message = json.loads(response.text)
            raise Exception(messages.ERROR_MESSAGE.format(message[constant.ERROR],message[constant.ERROR_DESCRIPTION]))

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
            raise Exception(messages.INVALID_REFRESH_TOKEN)

        response = requests.post(self.TOKEN_URL,
            data = {
                constant.CLIENT_ID:self.credentials[constant.CLIENT_ID],
                constant.CLIENT_SECRET:self.credentials[constant.CLIENT_SECRET],
                constant.REDIRECT_URI:'oob',
                constant.REFRESH_TOKEN:self.credentials[constant.REFRESH_TOKEN],
                constant.GRANT_TYPE:constant.REFRESH_TOKEN
            })
        if response.status_code == 200:
            self.load_token_response(response.text)
        else:
            message = json.loads(response.text)
            raise Exception(messages.ERROR_MESSAGE.format(message[constant.ERROR],message[constant.ERROR_DESCRIPTION]))