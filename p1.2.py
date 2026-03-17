import yfinance as yf

ticker = input("Which stock? ").upper()
stock = yf.Ticker(ticker)

price = stock.info.get("regularMarketPrice")
print(f"Latest price for {ticker}: {price}")