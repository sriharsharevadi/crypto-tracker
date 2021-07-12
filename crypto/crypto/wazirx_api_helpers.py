# importing the requests library
from datetime import datetime
from time import sleep

import pytz
import requests


def get_current_balance(coin_balance):
    r = requests.get(url="https://api.wazirx.com/api/v2/tickers", params=None)
    data = r.json()
    result = {}
    for key, value in coin_balance.items():
        if key.lower()+"inr" in data:
            result[key] = value*float(data.get(key.lower()+"inr").get("last"))
        elif key.lower()+"usdt" in data:
            result[key] = value*float(data.get(key.lower()+"usdt").get("last"))*float(data.get("usdtinr").get("last"))
        elif key.lower() == "inr":
            result[key] = value
        else:
            print("shit")

    return result


def get_price_at_time(market, time):
    # [timestamp,opening, highest, lowest, closing]
    # url = https://x.wazirx.com/api/v2/k?market=btcinr&period=1&limit=1&timestamp=1625504419
    # time_format = "2021-07-09 19:57:00"
    timestamp = time.replace(second=00).strftime("%s")
    params = {"market": market.lower(), "period": 1, "timestamp": timestamp}
    r = requests.get(url="https://x.wazirx.com/api/v2/k", params=params)
    data = r.json()
    res = None
    for i in data:
        if str(i[0]) == str(timestamp):
            res = (float(i[1]) + float(i[4]))/2

    if not res:
        params["limit"] = 200
        r = requests.get(url="https://x.wazirx.com/api/v2/k", params=params)
        data = r.json()

        for i in data:
            if str(i[0]) == str(timestamp):
                res = (float(i[1]) + float(i[4]))/2
        return res
    else:
        return res



