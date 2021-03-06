from modules import get_url
from modules import read_sheets
from modules import get_technipfmc_events

from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime

# Scrape Kws' financial calendar page to fetch financial events
def get_kws_calendar():

    # The earnings variable already contains the TechnipFMC events that's why we called the get_technipfmc_calendar function--which returns the earnings variable
    earnings = get_technipfmc_events.get_technipfmc_calendar()

    Comp_covered = read_sheets.read_GS('1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Companies covered!A2:D50', 'COLUMNS')

    # Create a new dict with companies' name as keys and companies' symbol as values
    Companies = Comp_covered['values'][0]
    Symbol = Comp_covered['values'][1]
    zip_comp_sym = zip(Companies, Symbol)
    list_comp_sym = list(zip_comp_sym)
    dict_comp_sym = dict(list_comp_sym)


    raw_html_kws = get_url.simple_get('https://www.kws.com/corp/en/company/investor-relations/financial-calendar/')

    html = soup(raw_html_kws, 'html.parser')

    list_container = html.find('div', attrs={'class': 'page'})

    # This first try/except catches the error in case there are no events on the company's calendar webpage
    try:

        for row in list_container.findAll('div', attrs={'class', 'block-content' }):
            for h3 in row.findAll('h4', attrs={'class', 'teaser-card__title h3'}):

                # We want the date format to be the same for each company so to sort events by date
                # Each company has its own date format. But some companies make it more difficult with some differences from one date to another
                # This try/except turn the 'usual date format' of Kws into a different one that we apply to all events. Except handles the unconventional situation
                try:

                    h3 = datetime.datetime.strptime(h3.text, '%B %d, %Y').strftime('%d-%b-%Y')

                    for h2 in row.findAll('h2', attrs={'class', 'h3'}):
                        for companies, symbol in dict_comp_sym.items():
                            if companies == 'Kws':

                                kws_earnings = ['Kws', symbol, h2.text, h3]
                                # We append Kws earnings's events to the earnings variable
                                earnings.append(kws_earnings)


                except ValueError:
                    h3 = h3.text

                    for h2 in row.findAll('h2', attrs={'class', 'h3'}):
                        for companies, symbol in dict_comp_sym.items():
                            if companies == 'Kws':

                                kws_earnings = ['Kws', symbol, h2.text, h3]

                                #We append Kws earnings's events to the global earnings variable
                                earnings.append(kws_earnings)

    except(AttributeError):
        earnings = []

    return earnings
