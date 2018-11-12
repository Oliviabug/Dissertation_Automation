from modules import get_date

import urllib
import urllib3
import requests
import json

#Quandl config
import quandl
quandl.ApiConfig.api_key = 'vn_2yd821asQwLbGhNVZ'
APIKEY = 'vn_2yd821asQwLbGhNVZ'


#Enter Quandl financial API to fetch the data we want
def Quandl_Request(database_code, dataset_code):

    #Quandl API: the three parameters we need
    start_date = get_date.get_date_time(-1)
    end_date = get_date.get_date_time(-1)
    APIKEY = 'vn_2yd821asQwLbGhNVZ'

    main_url = 'https://www.quandl.com/api/v3/datasets/' + database_code + '/' + dataset_code + '.json?'

    full_url = main_url + urllib.parse.urlencode({'start_date': start_date,'end_date': end_date, 'api_key': APIKEY})

    data = requests.get(full_url, verify=False)
    json_data = data.json()
    return json_data
