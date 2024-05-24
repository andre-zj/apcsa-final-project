from getData import get_stock_data
from getData import update_data
import usingdata
import user
import stock
import yfinance as yf
from datetime import datetime, timedelta, time

print("Welcome to our stock market simulator!")

name = input("What is your name?")

balance = float(input("What would you like to set your starting balance to"))

user = user(name, balance)

screen = input("Would you like to first use our stock screener? (y/n)")
if(screen == "y"):
    usingdata.stockScreener()

#add various stocks to portfolio
portfolio = []

while True:
    st = input("Enter the stock ticker of the stock you'd like to add to your portfolio (q to stop):")
    if st != "q":
        price = yf.Ticker(st)['currentPrice']
        amt = input('The stock is' + price + '. How many shares would you like to buy?')
        sto = stock(st, yf.Ticker(st))
        user.buy(sto, amt)
    else:
        break

#print("One minute in real life is equal to 15 minutes in the simulation (Runs for a max of 26 minutes)")
duration = int(input("Alright " + name + ", for how long do you want to run the simulation (in minutes)?"))

endTime = datetime.now() + timedelta(duration)
while(datetime.now() < endTime):
    for stock in user.portfolio:
        stock.update()
        print('The price of ' + stock.ticker + ' is: ' + stock.price)
    print(f"Updated portfolio at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(60)

#pushing

#run simulation for each stock in portfolio for this amount of time

