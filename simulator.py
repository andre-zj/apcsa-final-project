from getData import get_stock_data
from getData import update_data
import usingdata
import user
#import Stock as s
import yfinance as yf
from datetime import datetime, timedelta
import time

#import yfinance as yf
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


print("Welcome to our stock market simulator!")

name = input("What is your name?\n")

balance = float(input("What would you like to set your starting balance to:\n"))

user = user.user(name, balance)

screen = input("Would you like to first use our stock screener? (y/n)")
if(screen == "y"):
    usingdata.stockScreener()

portfolio = {}

while True:
    st = input("Enter the stock ticker of the stock you'd like to add to your portfolio (q to stop): ")
    if st.lower() != "q":
        stock_info = yf.Ticker(st).info
        if 'currentPrice' in stock_info:
            price = stock_info['currentPrice']
        else:
            print("Unable to retrieve current price for this stock. Please try another ticker.")
            continue

        amt = int(input(f'The stock is ${price}. How many shares would you like to buy? '))
        sto = Stock(st)
        user.buy(sto, amt)
        portfolio[st] = sto
    else:
        break

#print("One minute in real life is equal to 15 minutes in the simulation (Runs for a max of 26 minutes)")
duration = int(input("Alright " + name + ", for how long do you want to run the simulation (in minutes)?"))

endTime = datetime.now() + timedelta(duration)
while(datetime.now() < endTime):
    for st in user.stocks:
        st.update()
        current_price = st.price
        print(f"Updated price of {st.ticker}: {current_price}")

        initial_price = st.history['Close'][0]

        if current_price <= initial_price * 0.98:
            amount_to_buy = 10
            if amount_to_buy > 0:
                user.buy(st, amount_to_buy)
                print(f"Bought {amount_to_buy} shares of {st.ticker} at {current_price}")

        if current_price >= initial_price * 1.02:
            if st.ticker in user.portfolio and user.portfolio[st.ticker] > 0:
                user.sell(st, user.portfolio[st.ticker])
                print(f"Sold all shares of {st.ticker} at {current_price}")

    time.sleep(60) 

print(f"Final balance: {user.balance}")
print()
print("Final portfolio:")
for ticker, amount in user.portfolio.items():
    print(f"{ticker}: {amount} shares")


#run simulation for each stock in portfolio for this amount of time

