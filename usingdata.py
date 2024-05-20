import ast
import datetime as dt
import pandas as pd

with open('stock_info.txt', 'r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

allinfo = []
'''for line in lines:
    line.strip('{}')
    l = line.split(', ')
    info = {}
    for data in line:
        key, value = data.split(': ')
        info[key.strip()] = value.strip()
'''
for line in lines:
    info = ast.literal_eval(line)
    allinfo.append(info)

betalower = float(input('Enter lower Limit for Beta:\n'))
betaupper = float(input('Enter upper limit for Beta:\n'))

pricelower = float(input("what price must your share price be greater than?\n"))
priceupper = float(input("what price must your share price be less than?\n"))

print('marketCap options: micro, small, mid, large, mega')
marketCap = input("what must your marketCap be:\n")#adjust limits later

sector = input("what sector do you want your stock to be in?\n")

industry = input("what industry do you want your stock to be in?\n")

profitMargin = float(input("what are your specifications for your gross profit margin?\n"))

earningsGrowth = float(input('what are your specifications for your earnings growth\n'))

revenueGrowth = float(input("what are your specifications for your total revenue change\n"))


screened = []
unscreenedNones = []
for stock in allinfo:
    #implementation not correct for most
	#access each line in stocklist
    stockname = stock['symbol']
    #save name/ticker as stock
	
    try:
        #evaluating beta values of this stock is right
        if (stock['beta'] > betalower and stock['beta'] < betaupper):
            cond1 = True
        else:
            cond1 = False
        #evaluating if price of this stock is right
        thisPrice = stock['currentPrice'] #doesn't exist yet
        if(thisPrice > pricelower and thisPrice < priceupper): 
            cond2 = True
        else: 
            cond2 = False
        #evaluating if marketCap ration of this stock is right
        if (marketCap == 'micro' and stock['marketCap'] < 250000000):
            cond3 = True
        elif (marketCap =='small' and stock['marketCap'] < 2000000000 and stock['marketCap'] > 250000000):
            cond3 = True
        elif (marketCap == 'medium' and stock['marketCap'] > 2000000000 and stock['marketCap'] < 10000000000):
            cond3 = True
        elif (marketCap == 'large' and stock['marketCap'] > 10000000000 and stock['marketCap'] < 200000000000):
            cond3 = True 
        elif (marketCap == 'mega' and stock['marketCap'] > 200000000000):
            cond3 = True
        else:
            cond3 = False
        #evaluating if sector of this stock is right
        if (stock['sector'] == sector):
            cond4 = True
        else:
            cond4 = False
        #evaluating if industry is correct
        if (stock['industry'] == industry):
            cond5 = True
        else:
            cond5 = False
        #evaluating if profitMargin is correct
        if (stock['profitMargins'] > profitMargin):
            cond6 = True
        else:
            cond6 = False
        #evaluating if revenueChange is correct
        if (stock['earningsGrowth'] > earningsGrowth):
            cond7 = True
        else:
            cond7 = False
        #evaluating if earningsGrowth is correct
        if(stock['revenueGrowth'] > revenueGrowth):
            cond8 = True
        else:
            cond8 = False
        
        if(cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8):
            screened.append(stockname)

    except Exception:
        unscreenedNones.append(stockname)

for stock in screened:
    print(stock)






