import yfinance as yf
import pandas as pd
from pandas_datareader import pandas as pdr
import datetime as dt

file = open('stock_info.txt','t')

stocklist = file.readlines()
stocklist=stocklist.head()

beta = input("what range would you like your beta to be in?")
price = input("what price must your share price be greater than?")
pe = input("what must your price to earnings ratio be greater than?")
sector = input("what sector do you want your stock to be in?")
industry = input("what industry do you want your stock to be in?")

for i in stocklist.index:
	stock=str(stocklist["Symbol"][i])




