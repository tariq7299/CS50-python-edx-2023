import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
except requests.RequestException:
    sys.exit()

current_price = data['bpi']['USD']['rate_float']

amount_in_usd = amount * current_price

print(f"${amount_in_usd:,.4f}")
