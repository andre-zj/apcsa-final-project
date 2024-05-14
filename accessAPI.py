import requests
import yfinance as yf
import pandas as pd
import bokeh.plotting
#r = requests.get()

msft = yf.Ticker("MSFT")
print(msft.info)

stockslist = pd.read_csv('nasdaq_screener_1715521077293.csv')
names_col = 'Symbol'#Column names (what it says in the first row of the desired columns)
names = []
for row in range(1, stockslist.shape[0]):
    names.append(stockslist.at[row, names_col])

stocks = []
allInfo = []
for stock in names:
    try:
        unfiltered = yf.Ticker(stock).info
    except:
        print(stock + 'cannot be found')
    stocks.append(unfiltered)
    try:
        allInfo.append(stock, unfiltered['beta'], unfiltered['marketCap'], unfiltered['sector'], unfiltered['industry'], unfiltered['profitMargins'], unfiltered['earningsGrowth'], unfiltered['revenueGrowth'])
    except:
        print(stock + ' info cannot be completed')

    
for stock in allInfo:
    print(stock)

