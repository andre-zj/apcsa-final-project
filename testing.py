import yfinance as yf
stock = yf.Ticker('MSFT')
day = stock.history(period='2d', interval="1m")
print(day)