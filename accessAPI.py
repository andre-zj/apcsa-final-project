import yfinance as yf
import pandas as pd

stockslist = pd.read_csv('nasdaq_screener_1715521077293.csv')
names_col = 'Symbol'
names = []
for row in range(1, stockslist.shape[0]):
    names.append(stockslist.at[row, names_col])

stocks = []
allInfo = []
counter = 0
for stock in names:
    try:
        unfiltered = yf.Ticker(stock).info
        info = {
            'symbol': stock,
            'beta': unfiltered.get('beta', None),
            'marketCap': unfiltered.get('marketCap', None),
            'sector': unfiltered.get('sector', None),
            'industry': unfiltered.get('industry', None),
            'profitMargins': unfiltered.get('profitMargins', None),
            'earningsGrowth': unfiltered.get('earningsGrowth', None),
            'revenueGrowth': unfiltered.get('revenueGrowth', None)
        }
        allInfo.append(info)
    except Exception as e:
        print(f"Error retrieving info for {stock}: {e}")
        counter += 1
    
print(counter)
with open('stock_info.txt', 'w') as file:
    for stock in allInfo:
        file.write(str(stock) + '\n')

