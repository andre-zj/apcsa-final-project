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

<<<<<<< Updated upstream
betalower = float(input('Enter lower Limit for Beta:\n'))
betaupper = float(input('Enter upper limit for Beta:\n'))

pricelower = float(input("what price must your share price be greater than?\n"))
priceupper = float(input("what price must your share price be less than?\n"))
=======
betalower = float(input('Enter Lower Limit for Beta'))
betaupper = float(input('Enter upper limit for Beta'))

pricelower = float(input("what price must your share price be greater than?"))
priceupper = float(input("what price must your share price be less than?"))
>>>>>>> Stashed changes

print('marketCap options: micro, small, mid, large, mega')
marketCap = input("what must your marketCap be:\n")#adjust limits later

sector = input("what sector do you want your stock to be in?\n")

industry = input("what industry do you want your stock to be in?\n")

<<<<<<< Updated upstream
profitMargin = float(input("what are your specifications for your gross profit margin?\n"))

earningsGrowth = float(input('what are your specifications for your earnings growth\n'))

revenueGrowth = float(input("what are your specifications for your total revenue change\n"))


screened = []
for stock in allinfo:
=======
profitMargin = float(input("what are your specifications for your gross profit margin?"))

revenueChange = float(input("what are your specifications for your total revenue change"))

earningsGrowth = float(input('what are your specifications for your earnings growth'))


screened = []
counter = 0
'''r1 = input('Do you want to factor in beta? (y/n): ')
r2 = input('Do you want to factor in stock price? (y/n): ')
r3 = input('Do you want to factor in market cap? (y/n): ')
r4 = input('Do you want to factor in sector? (y/n): ')
r5 = input('Do you want to factor in industry? (y/n): ')
r6 = input('Do you want to factor in profit margin? (y/n): ')
r7 = input('Do you want to factor in revenue change? (y/n): ')
r8 = input('Do you want to factor in earnings growth? (y/n): ')'''
for stock in allinfo:

>>>>>>> Stashed changes
    #implementation not correct for most
	#access each line in stocklist
    stockname = stock['symbol']
    #save name/ticker as stock
	
	#evaluating beta values of this stock is right
<<<<<<< Updated upstream
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
    elif (marketCap == 'small' and stock['marketCap'] < 2000000000 and stock['marketCap'] > 250000000):
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
    #issue with odd character
    if (stock['industry'] > industry):
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
    if (stock['revenueGrowth'] > revenueGrowth):
        cond8 = True
    else:
        cond8 = False
	#evaluating if earningsGrowth is correct
=======
    try:
        if (stock['beta'] > betalower and stock['beta'] < betaupper):
            cond1 = True
        else:
            cond1 = False
    except Exception as e:
        cond1 = True
        #evaluating if price of this stock is right
    try:
        if(stock['currentPrice'] > pricelower and stock['currentPrice'] < priceupper): 
            cond2 = True
        else: 
            cond2 = False
    except Exception as e:
        cond2 = False
        #evaluating if marketCap ration of this stock is right
    try:
        if (marketCap == 'micro' and stock['marketCap'] < 250000000):
            cond3 = True
        elif (marketCap == 'small' and stock['marketCap'] < 2000000000 and stock['marketCap'] > 250000000):
            cond3 = True
        elif (marketCap == 'medium' and stock['marketCap'] > 2000000000 and stock['marketCap'] < 10000000000):
            cond3 = True
        elif (marketCap == 'large' and stock['marketCap'] > 10000000000 and stock['marketCap'] < 200000000000):
            cond3 = True
        elif (marketCap == 'mega' and stock['marketCap'] > 200000000000):
            cond3 = True
        else:
            cond3 = False
    except Exception as e:
        cond3 = False
        #evaluating if sector of this stock is right
    try:
        if (stock['sector'] == sector):
            cond4 = True
        else:
            cond4 = False
    except Exception as e:
        cond4 = True
        #evaluating if industry is correct
    try:
        if (stock['industry'] > industry):
            cond5 = True
        else:
            cond5 = False
    except Exception as e:
        cond5 = True
        #evaluating if profitMargin is correct
    try:
        if (stock['profitMargins'] > profitMargin):
            cond6 = True
        else:
            cond6 = False
    except Exception as e:
        cond6 = True
        #evaluating if revenueChange is correct
    try:
        if (stock['revenueGrowth'] > revenueChange):
            cond7 = True
        else:
            cond7 = False
    except Exception as e:
        cond7 = True
        #evaluating if earningsGrowth is correct
    try:
        if (stock['earningsGrowth'] > earningsGrowth):
            cond8 = True
        else:
            cond8 = False
    except Exception as e:
        cond8 = True
    if (stockname == 'MSFT'):
        print(cond1)
        print(cond2)
        print(cond3)
        print(cond4)
        print(cond5)
        print(cond6)
        print(cond7)
        print(cond8)
    if (cond1 == True and cond2 == True and cond3 == True and cond4 == True and cond5 == True and cond6 == True and cond7 == True and cond8 == True):
        screened.append(stock)
        #print(f"{stockname} has noneType data")
>>>>>>> Stashed changes

print(screened)



