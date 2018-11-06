from __future__ import print_function
import httplib2
from pprint import pprint
from googleapiclient import discovery

from modules import google_auth


discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
               'version=v4')
http = google_auth.get_credentials().authorize(httplib2.Http())
service = discovery.build('sheets', 'v4', credentials=google_auth.get_credentials())

#Read a range of cells from a specific spreadsheet
def read_GS(spreadsheet_id, range_name, major_dimension):
    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name, majorDimension = major_dimension)
    response = request.execute()
    return response
