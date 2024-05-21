import yfinance as yf
import pandas as pd
import datetime as dt

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history(period="5d", interval="1d")
    return df

def update_data(symbol):
    end_time = dt.now() + timedelta(minutes=duration_minutes)
    while dt.now() < end_time:
        stock_data = get_stock_data(symbol)
        current_price = stock_data['Close'].iloc[-1]
        
        # Example strategy: Buy if price drops, sell if price rises
        if current_price < simulator.portfolio.get(symbol, 0) * 0.95:  # Buy if price dropped by 5%
            simulator.buy_stock(symbol, 10, current_price)
        elif current_price > simulator.portfolio.get(symbol, 0) * 1.05:  # Sell if price increased by 5%
            simulator.sell_stock(symbol, 10, current_price)
        
        simulator.print_portfolio()
        print('Total Portfolio Value:', simulator.get_portfolio_value({symbol: current_price}))
        
        time.sleep(interval_seconds)

