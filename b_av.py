import requests
from dotenv import load_dotenv
import os

# create a .env file add AV_KEY=yourkey
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
    # print(k, " = ", data[k]["4. close"], type(data[k]["4. close"]))
    print(f"{k} = ${float(data[k]["4. close"]):.2f}")
    # 2024-12-18 = 220.1700