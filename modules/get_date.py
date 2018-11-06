#Get the date
import datetime

def get_date_time(days):
    day = datetime.timedelta(days=days)

    date = (datetime.datetime.now() + day).strftime("%Y-%m-%d")
    return date
