from modules import Quandl_request
from modules import read_sheets

#From Quanld API, only fetch the data we are interested in. Append the all the data into a list
def Filter_Quandl():

    #Empty list where will be appended the lists of data
    final_data = []

    #Fetch the symbol of the companies we cover from the right spreadsheet in order to filter the companies from Quandl API and only keep the ones we cover
    response = read_sheets.read_GS('1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Companies covered!B1:C400', 'COLUMNS')
    Sym = response['values'][0]
    Location = response['values'][1]
    list_Sym_Location = list(zip(Sym, Location))
    dict_Sym_Location = dict(list_Sym_Location)

    for sym, location in dict_Sym_Location.items():
        #We cover three index: Euronext, London stock exchange and the Frankfurt index.
        #The 'location' column will be different for each of the index.
        if location == 'Euro':
            Euronext_data = Quandl_request.Quandl_Request('EURONEXT', sym)

            #the next if loop is to check if the stock prices are indicated in the dataset because it's not always the case
            if Euronext_data['dataset']['data']:
                Euronext_open = Euronext_data['dataset']['data'][0][1]
                Euronext_close = Euronext_data['dataset']['data'][0][4]
                Companies_name = Euronext_data['dataset']['name']
                Stock_date = Euronext_data['dataset']['start_date']
                Euronext_data = [Companies_name, Stock_date, Euronext_open, Euronext_close]
                final_data.append(Euronext_data)

        elif location == 'UK':
            London_data = Quandl_request.Quandl_Request('XLON', sym)
            if London_data['dataset']['data']:
                London_open = London_data['dataset']['data'][0][1]
                London_close = London_data['dataset']['data'][0][4]
                Companies_name = London_data['dataset']['name']
                Stock_date = London_data['dataset']['start_date']
                London_data = [Companies_name, Stock_date, London_open, London_close]
                final_data.append(London_data)
                
        elif location == 'Germany':
            Fran_data = Quandl_request.Quandl_Request('FSE', sym)
            if Fran_data['dataset']['data']:
                Fran_open = Fran_data['dataset']['data'][0][1]
                Fran_close = Fran_data['dataset']['data'][0][4]
                Companies_name = Fran_data['dataset']['name']
                Stock_date = Fran_data['dataset']['start_date']
                Fran_data = [Companies_name, Stock_date, Fran_open, Fran_close]
                final_data.append(Fran_data)

    return final_data

print(Filter_Quandl())
