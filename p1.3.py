import yfinance as yf

for ticker in ['AMZN','TSLA','MSFT','AAPL','NVDA']:
    #ticker = 'AMZN'
    stock = yf.Ticker(ticker.upper())
    #print(stock)
    price = stock.info.get("regularMarketPrice")
    print(f"Stock price for {ticker} is {price}")