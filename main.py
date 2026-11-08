# The code shows how a TSX stock has performed over the past two years, represented in numbers and a chart
import yfinance as yf
import matplotlib.pyplot as plt

start_date = "2024-11-01" # Studying a 2 year period, dates are fixed for the research paper
end_date = "2026-11-07"
while True: # Introduce a loop which checks until a valid TSX ticker is found
    ticker = input("Choose a ticker to check daily and total returns\nEnter a TSX ticker: ").upper()
    if not ticker.endswith(".TO"): # Add .TO if not added because TSX stocks need it on Yahoo Finance
       ticker = ticker + ".TO"
    data = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval="1d", 
        auto_adjust=True, # This will adjust for dividends and splits
        progress=False,
        multi_level_index=False,
    )
    
    if data.empty: # Checks if athe download is empty. Could be a bad ticker or no internet
        print("No data found. Check the ticker or internet connection")
    else:
        break

prices = data["Close"]
returns = prices.pct_change().dropna() # Daily returns is how much the price changed from one day to the next. .dropna() is placed because the first day has no previous day
print(returns)

overall_return = prices.iloc[-1] / prices.iloc[0] - 1 # Total return , used the formula last / first -1
print(f"Total return: {round(overall_return * 100, 2)}%")

prices.plot(label="Prices") 
ma50 = prices.rolling(50).mean() # The average of last 50 closing prices
ma50.plot(label="50-day MA")
plt.title(ticker + " Stock Price")
plt.ylabel("Adjusted Price (CAD)")
plt.xlabel("Date")
plt.legend()
plt.show()
