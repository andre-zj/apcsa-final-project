import requests
import yfinance as yf
import pandas as pd
import bokeh.plotting
#r = requests.get()

msft = yf.Ticker("MSFT")
print(msft.info)

stockslist = pd.read_csv('nasdaq_screener_1715521077293.csv')
names = 'Symbol'#Column names (what it says in the first row of the desired columns)

stocks = []
for stock in names:
    stocks.append(yf.Ticker(stock).info)

allInfo = []
for stock in stocks:
    info = []
    info.append(stock['beta'], stock['marketCap'], stock['sector'], stock['industry'], stock['profitMargins'], stock['earningsGrowth'], stock['revenueGrowth'])
    
for stock in info:
    print(stock)

