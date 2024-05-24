class user:
    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance
        self.portfolio = {}
        self.stocks = []
    
    def buy(self, stock, amount):
        if stock.ticker in self.portfolio:
            self.portfolio[stock.ticker] += amount
        else:
            self.portfolio[stock.ticker] = amount
        self.balance -= stock.price * amount
        if stock not in self.stocks:
            self.stocks.append(stock)
    
    def buy2(self, stock, money):
        amount = int(money/stock)
        if stock.ticker in self.portfolio:
            self.portfolio[stock.ticker] += amount
        else:
            self.portfolio[stock.ticker] = amount
        balance -= stock.price * amount
        if stock not in self.stocks:
            self.stocks.append(stock)
    
    def sell(self, stock, amount):
        if self.portfolio[stock.ticker] < amount:
            print("you don't have that much stock")
        elif self.portfolio[stock.ticker] > amount:
            self.portfolio[stock.ticker] -=amount
            balance += stock.price * amount
        else:
            self.portfolio[stock.ticker] = 0
            balance += stock.price * amount
    
    def sell2(self, stock, money):
        amount = int(money/stock)
        if self.portfolio[stock.ticker] < amount:
            print("you don't have that much stock")
        elif self.portfolio[stock.ticker] > amount:
            self.portfolio[stock.ticker] -=amount
            balance += stock.price * amount
        else:
            self.portfolio[stock.ticker] = 0
            balance += stock.price * amount

#keep share options/delete price based