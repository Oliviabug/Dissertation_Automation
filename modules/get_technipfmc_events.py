from modules import get_url
from modules import read_sheets

from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime

earnings = []

def get_technipfmc_calendar():

    Comp_covered = read_sheets.read_GS('1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Companies covered!A2:D50', 'COLUMNS')

    #Create a new dict with companies name as key and companies symbol as value
    Companies = Comp_covered['values'][0]
    Symbol = Comp_covered['values'][1]
    zip_comp_sym = zip(Companies, Symbol)
    list_comp_sym = list(zip_comp_sym)
    dict_comp_sym = dict(list_comp_sym)

    Events_onTheGS = read_sheets.read_GS('1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Calendar!A2:D50', 'COLUMNS')

    #Create a new list containing the events already on the worksheet so we can remove duplicates
    Companies = Events_onTheGS['values'][0]
    Symbol = Events_onTheGS['values'][1]
    Event_Desc = Events_onTheGS['values'][2]
    Event_Date = Events_onTheGS['values'][3]
    zip_events = zip(Companies, Symbol, Event_Desc, Event_Date)
    list_events = list(zip_events)
    print(list_events)

    raw_html_technipfmc = get_url.simple_get('http://investors.technipfmc.com/phoenix.zhtml?c=254471&p=irol-calendar')

    #Once we have the raw HTML, we start to select and extract
    html = soup(raw_html_technipfmc, 'html.parser')
    main = html.find('main',attrs={"id":"maincontent"})

    try:
        calendar_div = main.find('div', attrs={"class": "event-item-details"})
        earning_title = calendar_div.find('h5', attrs={"class", "event-item-details-title"})
        earning_date = calendar_div.find('p', attrs={"class", "event-item-details-date"})

    #   Get the right format for the date so we can sort them and remove thr outdated events
        earning_date = datetime.datetime.strptime(earning_date.text, '%B %d, %Y\xa01:00 p.m.\xa0UKT').strftime('%d-%b-%Y')

        for companies, symbol in dict_comp_sym.items():
            if companies == 'Technipfmc':
                technipfmc_earnings = ['Technipfmc', symbol, earning_title.text, earning_date]
                #This loop will prevent duplicate
                if technipfmc_earnings not in list_events:

                    #We want to retrieve h5 the title and p the description with the date
                    earnings.append(technipfmc_earnings)


    except(AttributeError):
        earnings = []

    return earnings
