import json
import requests
import webbrowser

class YahooOAuth:
    AUTH_URL = 'https://api.login.yahoo.com/oauth2/request_auth?client_id={0}&redirect_uri=oob&response_type=code&language=en-us'
    TOKEN_URL = 'https://api.login.yahoo.com/oauth2/get_token'

    def __init__(self, credentials: str):
        """ Constructor.

        Parameters
        ----------
        credentials : str
            The name of the json file containing client credentials.
        """
        self.credentials_file
        data = json.loads(credentials)
        self.client_id = data['client_id']
        self.client_secret = data['client_secret']
        self.auth_code = data['auth_code']
    
    def get_auth_code(self):
        """ Gets authorization code from API. 
        Requires user to login to Yahoo account, allow access and enter auth code.
        """
        auth_url = self.AUTH_URL.format(self.client_id)
        webbrowser.open(auth_url)
        self.auth_code = input('Enter authorization code: ')
        file = open(self.credentials_file)
        data = json.load(file)
        file.close()
        data['auth_code'] = self.auth_code
        with open(self.credentials_file, 'w') as credentials_file:
            json.dump(data, credentials_file, indent=4)
    
    def was_auth_code_obtained(self):
        """Checks whether the authorization code was already obtained or not.

        Returns
        -------
        boolean
            True if the authorization code was already obtained, false otherwise.
        """
        if len(self.auth_code) > 0:
            return True
        else:
            return False
    
    def load_token_response(self, text : str):
        """Loads access token response from Yahoo.

        Parameters
        ----------
        text : str
            The server response text.
        """
        data = json.loads(text)
        self.access_token = data['access_token']
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        self.refresh_token = data['refresh_token']
        self.expires_in = data['expires_in']
        self.token_type = data['token_type']
        self.xoauth_yahoo_guid = data['xoauth_yahoo_guid']
        self.date_obtained = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
        data['date_obtained'] = str(self.date_obtained)
        with open('token.json', 'w') as token_file:
            json.dump(data, token_file, indent=4)

    def fetch_access_token(self):
        """Fetch the access token using the stored authorization code."""
        if len(self.auth_code) == 0:
            raise Exception('A valid authorization code is required to get the access token.')
        else:
            response = requests.post(self.TOKEN_URL,
                data = {
                    'grant_type':'authorization_code',
                    'code':self.auth_code,
                    'redirect_uri':'oob',
                    'client_id':self.client_id,
                    'client_secret':self.client_secret
                })
            if response.status_code == 200:
                self.load_token_response(response.text)
                return self.access_token
            else:
                print('An error occured while obtaining an access token.') # maybe raise an exception?
    
    def is_token_valid(self):
        now_in_seconds = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
        time_remaining = (now_in_seconds - int(self.date_obtained))
        if time_remaining > self.expires_in:
            return False
        else:
            return True

    def refresh_access_token(self):
        response = requests.post(self.TOKEN_URL,
            data = {
                'client_id':self.client_id,
                'client_secret':self.client_secret,
                'redirect_uri':'oob',
                'refresh_token':self.refresh_token,
                'grant_type':'refresh_token'
            })
        if response.status_code == 200:
            self.load_token_response(response.text)
            return self.access_token
        else:
            print('An error occured while trying to refresh token.')
    
            