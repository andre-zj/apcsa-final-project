from getData import get_stock_data
from getData import update_data
import usingdata
import user
from datetime import datetime, timedelta
import time

print("Welcome to our stock market simulator!")

name = input("What is your name?\n")

balance = float(input("What would you like to set your starting balance to:\n"))

user = user.user(name, balance)

screen = input("Would you like to first use our stock screener? (y/n)")
if(screen == "y"):
    usingdata.stockScreener()

#add various stocks to portfolio
portfolio = {}


while True:
    st = input("Enter the stock ticker of the stock you'd like to add to your portfolio (q to stop):")
    if st != "q":
        portfolio.append(st)
        #add objects and make dictionary with share number
    else:
        break

duration = int(input("Alright " + name + ", for how long do you want to run the simulation (in minutes)?"))

endTime = datetime.now() + timedelta(duration)
while(datetime.now() < endTime):
    for st in portfolio:
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
print("Final portfolio:")
for ticker, amount in user.portfolio.items():
    print(f"{ticker}: {amount} shares")


#run simulation for each stock in portfolio for this amount of time

