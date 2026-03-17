import requests
# https://api.coinbase.com/v2/exchange-rates?currency=BTC
# https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
price = requests.get(url).json()['bitcoin']['usd']
print(f"Bitcoin: ${price:,.2f}")