import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

api_key = "1de6e9acbde2c3b664287d1dbed80720ab64435be6fe8492b4abc436f4c9d84a"
url = "https://rest.coincap.io/v3/assets/bitcoin"
headers = {"Authorization": f"Bearer {api_key}"}

try:
    resp = requests.get(url, headers = headers, timeout = 10)
    resp.raise_for_status()
except requests.RequestException as e:
    sys.exit(f"Request failed: {e}")

data = resp.json()

try:
    price_usd = float(data["data"]["priceUsd"])
    total_value = price_usd * amount
    print(f"${total_value:,.4f}")
except (KeyError, TypeError, ValueError):
    pass




