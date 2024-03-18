from ast import Str
import yfinance as yf
import pandas as pd
import datetime as dt

def get_raw_data(name :str):
    start_date = dt.datetime(2019, 9, 10)
    end_date = dt.datetime.today()

    # Fetch data using yfinance
    raw_data = yf.download(name, start=start_date, end=end_date)

    return raw_data
