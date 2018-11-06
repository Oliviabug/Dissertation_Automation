from modules import get_url
from modules import read_sheets
from modules import get_kws_events

from bs4 import BeautifulSoup as soup
import pandas as pd

#Get the events from Puma and append them into the earnings variable
def get_puma_calendar():

    earnings = get_kws_events.get_kws_calendar()

    Comp_covered = read_sheets.read_GS('1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Companies covered!A2:D50', 'COLUMNS')

    #Create a new dict with companies name as key and companies symbol as value
    Companies = Comp_covered['values'][0]
    Symbol = Comp_covered['values'][1]
    zip_comp_sym = zip(Companies, Symbol)
    list_comp_sym = list(zip_comp_sym)
    dict_comp_sym = dict(list_comp_sym)

    raw_html_puma = get_url.simple_get('https://about.puma.com/en/investor-relations/calendar')

    #Once we have the raw HTML, we start to select and extract
    html = soup(raw_html_puma, 'html.parser')

    list_container = html.find('div',attrs={"class":"article-list-container"})

    try:

        for row in list_container.findAll('div', attrs={'class', 'text'}) :
            for p in row.findAll('p', attrs={'class', 'date'}):
                for h3 in row.findAll('h3'):
                    for companies, symbol in dict_comp_sym.items():
                        if companies == 'Puma':
                            Puma_earnings = ['Puma', symbol, h3.text, p.text]
                            earnings.append(Puma_earnings)

    except:
        earnings = []

    return earnings
