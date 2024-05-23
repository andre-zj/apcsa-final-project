import yfinance as yf
import pandas as pd
import datetime as dt
import time as t

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history(period="1d", interval="1m")
    return df

def update_data(symbol):
    stock_data = get_stock_data(symbol)
    current_price = stock_data['Close'].iloc[-1]
    return current_price
    

