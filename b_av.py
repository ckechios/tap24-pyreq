import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://www.alphavantage.co/query"

AVKEY = os.environ["AV_KEY"]
# print("AV key used:", AVKEY)

params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "IBM",
    "apikey" : AVKEY
}

response = requests.get(API_URL, params)
print(response)

rr = response.json()

data = rr['Time Series (Daily)']

for k in data:
    print(k, " = ", data[k])
    # 2024-12-18 = 220.1700