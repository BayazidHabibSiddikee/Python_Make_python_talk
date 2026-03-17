from yahoo_fin import stock_info as si 
while True:
    #Obtain ticker symbol for you
    ticker = input("Which stock (ticker symbol) are you looking for?\n>>>")
    # If you want to stop, type in "done"
    if ticker=='done':
        break
    else:
        #Obtain stock price from yahoo
        price = si.get_live_price(ticker)
        print(f"Stock price is: {price}",font=('Arial',20,'bold'))