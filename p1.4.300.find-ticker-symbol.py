#  https://query1.finance.yahoo.com/v1/finance/search?q=
from mptpkg import print_say
import requests, sys
import yfinance as yf
firm = 'jpmorgan chase'   # input("Which company?\n>>>").lower()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
if firm == 'done':
    sys.exit()
else:
    try:
        url = f"https://query1.finance.yahoo.com/v1/finance/search?q={firm}"
        response = requests.get(url,headers=headers)
        res = response.json()
        symbol = res['quotes'][0]['symbol']
        #print(res['quotes'])
        #print(symbol)
        stock = yf.Ticker(symbol)
        price = stock.info.get("regularMarketPrice")
        say = f"Price of {firm}, Ticker {symbol} is {price}$"
        print_say(say)
    except:
        print_say("Sorry not a valid entry!")
