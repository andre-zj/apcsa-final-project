import datetime as dt

with open('stock_info.txt', 'r') as file:
    lines = file.readlines()

print('beta options: <-0.2, -0.2 to 0.2, 0.2 to 0.8, 0.8 to 1.2, 1.2 to 2.0, > 2.0')
beta = input("what range would you like your beta to be in?")

price = input("what price must your share price be greater than?")

print('marketCap options: small, mid, large, mega')
marketCap = input("what must your marketCap be greater than?")

sector = input("what sector do you want your stock to be in?")

industry = input("what industry do you want your stock to be in?")

profitMargin = input("what are your specifications for your gross profit margin?")

revenueChange = input("what are your specifications for your total revenue change")

earningsGrowth = input('what are your specifications for your earnings growth')


screened = []
for line in lines:
    #implementation not correct for most
	#access each line in stocklist
    stock = line['symbol']
    #save name/ticker as stock
	
	#evaluating beta values of this stock is right
    
	#evaluating if price of this stock is right
    thisPrice = line['price'] #doesn't exist yet
    if(thisPrice > price): 
        cond2 = True
    else: 
        cond2 = False
	#evaluating if marketCap ration of this stock is right
    thisCap = line['marketCap']

	#evaluating if sector of this stock is right
    
	#evaluating if profitMargin is correct
    
	#evaluating if revenueChange is correct
    
	#evaluating if earningsGrowth is correct
		







