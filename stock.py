import yfinance as yf
class Stock: 
    def __init__ (self, t):
        self.ticker = t
        self.info = yf.Ticker(t)
        self.history = self.info.history(period='1d', interval='1m')
        self.price = self.history['Close'].iat[0]
        self.minute = 0
    
    def update (self):
        if (self.minute < 390):
            self.minute +=1
            self.price = self.history.iat[self.minute, 1]
        else:
            print('day end!')
    
    def reset (self):
        self.history = self.info.history(period='1d', interval="1m")
        self.price = self.history.iat[0, 1]
        self.minute = 0
