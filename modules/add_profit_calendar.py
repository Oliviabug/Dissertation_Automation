from modules import add_journalists_calendar
import xlrd
import collections


#add the last quarter profit of the company to allow quick comparison when we report results for example.
def add_profit():

    earnings= add_journalists_calendar.add_journalists()

    #The data are fetched from an Excel file
    loc = ("Quarter_profit.xlsx")
    Quarter_profit = collections.defaultdict(list)
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    for i in range(sheet.nrows):

        Comp_symbol = sheet.cell_value(i, 0)
        Comp_net_profit = sheet.cell_value(i, 1)


        if sheet.cell(i, 1).ctype == 5:
            Comp_net_profit = None
        else:
            Comp_net_profit = sheet.cell_value(i, 1)

        Quarter_profit[Comp_symbol].append(Comp_net_profit)

    #As for the journalists name, the data are added into the already existing list of lists variable named earnings
    for lists in earnings:
        for ele in lists:
            for symbol, profit in Quarter_profit.items():
                    if ele == symbol:
                        lists.append(profit[0])


    return earnings

print(add_profit())
