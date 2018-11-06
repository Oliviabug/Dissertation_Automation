from __future__ import print_function
import httplib2
from pprint import pprint
from googleapiclient import discovery

from modules import google_auth


discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
               'version=v4')
http = google_auth.get_credentials().authorize(httplib2.Http())
service = discovery.build('sheets', 'v4', credentials=google_auth.get_credentials())

#Update a range of cells from a specific Google Sheet
def GS_Update(value, spreadsheet_id, range_name):

    #How the data should be interpreted
    value_input_option = 'USER_ENTERED'


    values = value


    body = {'values': values}

    request_other = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_name,
                                                     valueInputOption= value_input_option,
                                                     body = body)

    response = request_other.execute()

    pprint(response)
