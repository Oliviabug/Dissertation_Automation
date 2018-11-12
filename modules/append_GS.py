from __future__ import print_function
import httplib2
from pprint import pprint
from googleapiclient import discovery

from modules import google_auth


discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
               'version=v4')

http = google_auth.get_credentials().authorize(httplib2.Http())
service = discovery.build('sheets', 'v4', credentials=google_auth.get_credentials())

#Add our data (value) to Google Sheet (spreadsheet_id)
def GS_Append(value, spreadsheet_id, range_name):

    #How the data should be interpreted
    value_input_option = 'USER_ENTERED'


    values = value


    body = {'values': values}

    request_other = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_name,
                                                     valueInputOption= value_input_option,
                                                     body = body)

    response = request_other.execute()

    pprint(response)
