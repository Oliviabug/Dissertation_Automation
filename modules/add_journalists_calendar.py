from modules import get_technipfmc_events
from modules import get_kws_events
from modules import get_puma_events
from modules import read_sheets


#Append the name of the journalist by comparison with another spreadsheet where joutnalists are bound to companies--The ones they cover
def add_journalists():

    earnings = get_puma_events.get_puma_calendar()

    Comp_covered = read_sheets.read_GS('1zblGlPcVVZQJIOWHaGlsSpVU9gp3t1rXRDDqZaED1QI', 'Companies covered!A2:D50', 'COLUMNS')

    #Create a dict with companies name as key and the journalist covering the company as value
    Companies = Comp_covered['values'][0]
    Journalist = Comp_covered['values'][3]
    zip_comp_journalist = zip(Companies, Journalist)
    list_comp_journalist = list(zip_comp_journalist)
    dict_comp_journalist = dict(list_comp_journalist)

    #Add the journalist name into the already existing list of list named earnings
    for lists in earnings:
        for ele in lists:
            for companies, journalists in dict_comp_journalist.items():
                if ele == companies:
                    lists.append(journalists)

    print(earnings)
    return earnings
