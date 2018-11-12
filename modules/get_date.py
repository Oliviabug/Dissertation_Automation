#Get the date
import datetime

# The 'days' parameter allow us to fetch a past or future date 
def get_date_time(days):
    day = datetime.timedelta(days=days)

    date = (datetime.datetime.now() + day).strftime("%Y-%m-%d")
    return date
