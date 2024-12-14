import sys
import requests


def main():
    try:
        if len(sys.argv) == 2:
            bitcoin = float(sys.argv[1])
            bitcoin_api(bitcoin)
        else:
            sys.exit(1)
    except ValueError:
        sys.exit(1)


def bitcoin_api(bitcoin):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    usd = data["bpi"]["USD"]["rate_float"]

    calc = usd * bitcoin
    print(f"${calc:,.4f}")


main()
