from googleapiclient import discovery
from googleapiclient import errors
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client import file 

import os

import warnings
warnings.filterwarnings('ignore')

#Set the scopes and Google authentication
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://spreadsheets.google.com/feeds']
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Newsroom_automation'

import argparse
flags = tools.argparser.parse_args([])

discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
               'version=v4')

# Get the credential to access and modify Google sheets
def get_credentials():

    # You will have to change the home_dir variable when you will run the script as it's my own local directory here
    home_dir = os.path.expanduser('~oliviabugault')
    credentials_dir = os.path.join(home_dir, '.credentials')

    if not os.path.exists(credentials_dir):
        os.makedirs(credentials_dir)
    credentials_path = os.path.join(credentials_dir,
                                    'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credentials_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credentials_path)

    #The credentials authorize me to access and use the Google Sheet API (as well as other Google APIs potentially)
    return credentials
