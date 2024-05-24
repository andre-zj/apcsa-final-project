class stock: 
    def __init__ (self, t, info):
        self.ticker = t
        self.info = info
        self.history = info.history(period='1d', interval="1m")
        self.price = self.history.iat[0, 1]
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
