from datetime import datetime

import openpyxl
from multiprocessing import Pool
from crypto.wazirx_api_helpers import get_current_balance, get_price_at_time

path = "harsha.xlsx"

# workbook object is created
wb_obj = openpyxl.load_workbook(path)

ech_trades = wb_obj.get_sheet_by_name('Exchange Trades')
acc_balance = wb_obj.get_sheet_by_name('Account Balance')

# iterate through excel and display data
coin_balance = {}
for row in acc_balance.iter_rows(min_row=2, min_col=1, max_row=acc_balance.max_row, max_col=2):
    coin_balance[row[0].value] = row[1].value
    # for cell in row:
    #     print(cell.value, end=" ")


# result = get_current_balance(coin_balance)


# total = 0
# for key in result:
#     total = total + result[key]
#
# print(int(total))

orders = []
for row in ech_trades.iter_rows(min_row=2, min_col=1, max_row=ech_trades.max_row, max_col=ech_trades.max_column):
    temp = []
    for i in row:
        temp.append(i.value)
    orders.append(temp)
def process_order(i):
    if "inr" in i[1].lower():
        price = get_price_at_time("usdtinr", i[0])
        return i
    elif "usdt" in i[1].lower():
        price = get_price_at_time("usdtinr", i[0])
        i[2] = i[2]*price
        return i
    elif "wrx" in i[1].lower():
        price = get_price_at_time("wrxinr", i[0])
        i[2] = i[2]*price
        return i
    elif "btc" in i[1].lower():
        price = get_price_at_time("btcinr", i[0])
        i[2] = i[2]*price
        return i
    else:
        return "shit"

def price_in_inr(orders):
    orders_pool = Pool(len(orders))
    results = orders_pool.map(process_order, orders)
    return results

price_in_inr(orders)
print(datetime.now())
