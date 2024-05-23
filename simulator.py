from getData import get_stock_data
from getData import update_data
import usingdata
import user
from datetime import datetime, timedelta

print("Welcome to our stock market simulator!")

name = input("What is your name?")

balance = float(input("What would you like to set your starting balance to"))

user = user(name, balance)

screen = input("Would you like to first use our stock screener? (y/n)")
if(screen == "y"):
    usingdata.stockScreener()

#add various stocks to portfolio
portfolio = []

duration = int(input("Alright " + name + ", for how long do you want to run the simulation (in minutes)?"))

endTime = datetime.now() + timedelta(duration)
while(datetime.now() < endTime):
    for stock in portfolio:
        currentPrice = update_data(stock)
        
#run simulation for each stock in portfolio for this amount of time

