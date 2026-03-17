import requests

url = "https://query1.finance.yahoo.com/v1/finance/search?q=amazon"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.json()["quotes"][0]["symbol"])
