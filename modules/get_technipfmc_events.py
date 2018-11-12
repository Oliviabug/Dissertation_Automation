from modules import get_url
from modules import read_sheets

from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime

#Creation of earnings variable--empty so far-- where will be appended all the lists of events
earnings = []

# Scrape TechnipFMC's financial calendar webpage to fetch financial events
def get_technipfmc_calendar():

    Comp_covered = read_sheets.read_GS('1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Companies covered!A2:D50', 'COLUMNS')

    #Create a new dict with companies' name as keys and companies' symbol as values
    Companies = Comp_covered['values'][0]
    Symbol = Comp_covered['values'][1]
    zip_comp_sym = zip(Companies, Symbol)
    list_comp_sym = list(zip_comp_sym)
    dict_comp_sym = dict(list_comp_sym)

    raw_html_technipfmc = get_url.simple_get('http://investors.technipfmc.com/phoenix.zhtml?c=254471&p=irol-calendar')

    # Once we have the raw HTML, we start to select and extract
    html = soup(raw_html_technipfmc, 'html.parser')
    main = html.find('main',attrs={"id":"maincontent"})

    # This try/except catches the error in case there are no events on the company's calendar webpage
    try:
        calendar_div = main.find('div', attrs={"class": "event-item-details"})
        earning_title = calendar_div.find('h5', attrs={"class", "event-item-details-title"})
        earning_date = calendar_div.find('p', attrs={"class", "event-item-details-date"})

        # Get the right format for the date so we can sort them and remove the outdated events
        earning_date = datetime.datetime.strptime(earning_date.text, '%B %d, %Y\xa01:00 p.m.\xa0UKT').strftime('%d-%b-%Y')

        for companies, symbol in dict_comp_sym.items():
            if companies == 'Technipfmc':
                technipfmc_earnings = ['Technipfmc', symbol, earning_title.text, earning_date]

                earnings.append(technipfmc_earnings)

    except(AttributeError):
        earnings = []

    return earnings
