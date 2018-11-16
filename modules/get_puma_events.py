from modules import get_url
from modules import read_sheets
from modules import get_kws_events

from bs4 import BeautifulSoup as soup
import pandas as pd

# Scrape Puma's financial calendar webpage to fetch financial events
def get_puma_calendar():

    # The earnings variable already contains the TechnipFMC and Kws events that's why we called the get_kws_calendar function--which returns the earnings variable
    earnings = get_kws_events.get_kws_calendar()

    Comp_covered = read_sheets.read_GS('1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Companies covered!A2:D50', 'COLUMNS')

    #Create a new dict with companies name as key and companies symbol as value
    Companies = Comp_covered['values'][0]
    Symbol = Comp_covered['values'][1]
    zip_comp_sym = zip(Companies, Symbol)
    list_comp_sym = list(zip_comp_sym)
    dict_comp_sym = dict(list_comp_sym)

    #This following piece of script was supposed to remove the duplicates and only append the new events but I couldn't make it completely functional

    # Events_onTheGS = read_sheets.read_GS('1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Calendar!A2:D50', 'COLUMNS')
    #
    # try:
    #
    #     Companies = Events_onTheGS['values'][0]
    #     Symbol = Events_onTheGS['values'][1]
    #     Event_Desc = Events_onTheGS['values'][2]
    #     Event_Date = Events_onTheGS['values'][3]
    #     zip_events = zip(Companies, Symbol, Event_Desc, Event_Date)
    #     #list_events variabe contains the events already on the GS
    #     list_events = list(zip_events)
    #     for events in list_events:
    #         events=list(events)
    # except(KeyError):
    #     list_events=[]

    raw_html_puma = get_url.simple_get('https://about.puma.com/en/investor-relations/calendar')

    #Once we have the raw HTML, we start to select and extract
    html = soup(raw_html_puma, 'html.parser')

    list_container = html.find('div',attrs={"class":"article-list-container"})

    # This try/except catches the error in case there are no events on the company's calendar webpage
    try:

        for row in list_container.findAll('div', attrs={'class', 'text'}) :
            for p in row.findAll('p', attrs={'class', 'date'}):
                for h3 in row.findAll('h3'):
                    for companies, symbol in dict_comp_sym.items():
                        if companies == 'Puma':
                            Puma_earnings = ['Puma', symbol, h3.text, p.text]

                            #We append Puma earnings's events to the earnings variable
                            earnings.append(Puma_earnings)




    except(AttributeError):
        earnings = []

    return earnings
