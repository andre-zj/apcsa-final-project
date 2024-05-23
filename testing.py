import yfinance as yf
stock = yf.Ticker('MSFT')
day = stock.history(period='1d', interval="1m")
with open('test.txt', 'w') as file:
    file.write(day)