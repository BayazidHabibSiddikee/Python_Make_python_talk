import yfinance as yf

company = {"amazon":'AMZN','facebook':'META','Tesla':'TSLA','google':'GOOGL','Apple':'AAPL'}
for name, ticker in company.items():
    stock = yf.Ticker(ticker)
    
    #Get price
    price = stock.info.get("regularMarketPrice")
    print(f"Company {name} has stock price {price}$")
    
    # live price another way
    print(stock.info['regularMarketPrice'])
    
    #Historical price
    print("Historical price")
    print(stock.history(period="5y"))
    # or
    #print(stock.history(start="2015-01-01",end='2025-12-10'))
    # or
    #print(stock.history(interval="1wk",period="10y"))
    
    #Earnings calendar
    print("Earnings calendar")
    print(stock.earnings_dates)
    
    #Quarterly and yearly financials
    #Income statements
    print("Income statements")
    print(stock.financials) #yearly
    print(stock.quarterly_financials) #half yearly
    
    #balance sheet
    print("Balance sheet")
    print(stock.balance_sheet)
    print(stock.quarterly_balance_sheet)
    
    #cash flow
    print("Cash flow")
    print(stock.cashflow)
    print(stock.quarterly_cashflow)
    
    # recommendations
    print("Recommendations")
    print(stock.recommendations)
    print(stock.recommendations_summary)
    
    #Download full chart
    data = yf.download(ticker,start="2015-01-01",end="2025-12-10")
    print(data)