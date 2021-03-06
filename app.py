#Modules to import from modules folder
from modules import Update_GS
from modules import Filter_Quandl_data
from modules import add_journalists_calendar
from modules import get_puma_events
from modules import append_GS
from modules import add_profit_calendar


#This function will update the stock market data on the 'Stock' worksheet - only for the companies we cover
Update_GS.GS_Update(Filter_Quandl_data.Filter_Quandl(),'1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Stock!A2:D200')

#This function will scrape Puma's website to find the date of its financial events. We only call Puma because it triggers the other companies function/module
get_puma_events.get_puma_calendar()

#This function adds the name of the journalists who cover the companies on the 'Calendar' worksheet
add_journalists_calendar.add_journalists()

#This final function appends--update--all the data we fetched from APIs/Excel on our Google Sheet.
Update_GS.GS_Update(add_profit_calendar.add_profit(), '1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Calendar!A2:H200')
