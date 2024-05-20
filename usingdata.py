import ast
import datetime as dt
with open('stock_info.txt', 'r') as file:
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

betalower = int(input('Enter Lower Limit for Beta'))
betaupper = int(input('Enter upper limit for Beta'))

pricelower = int(input("what price must your share price be greater than?"))
priceupper = int(input("what price must your share price be less than?"))

print('marketCap options: micro, small, mid, large, mega')
marketCap = input("what must your marketCap be greater than?")#adjust limits later

sector = input("what sector do you want your stock to be in?")

industry = input("what industry do you want your stock to be in?")

profitMargin = int(input("what are your specifications for your gross profit margin?"))

revenueChange = int(input("what are your specifications for your total revenue change"))

earningsGrowth = int(input('what are your specifications for your earnings growth'))


screened = []
counter = 0
for stock in allinfo:
    #implementation not correct for most
	#access each line in stocklist
    stockname = stock['symbol']
    #save name/ticker as stock
	
	#evaluating beta values of this stock is right
    try:
        if (stock['beta'] > betalower and stock['beta'] < betaupper):
            cond1 = True
        else:
            cond1 = False
        #evaluating if price of this stock is right
        if(stock['currentPrice'] > pricelower and stock['currentPrice'] < priceupper): 
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
        if (stock['revenueGrowth'] > revenueChange):
            cond7 = True
        else:
            cond7 = False
        #evaluating if earningsGrowth is correct
        if (stock['earningsGrowth'] > earningsGrowth):
            cond8 = True
        else:
            cond8 = False
        if (cond1 == True and cond2 == True and cond3 == True and cond4 == True and cond5 == True and cond6 == True and cond7 == True and cond8 == True):
            screened.append(stock)
    except Exception as e:
        counter += 1
        #print(f"{stockname} has noneType data")

print(screened)



