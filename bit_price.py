import sys
import requests

api_key = "ae79516d446a470692cfd7e6d99aae366cf6a99eb69e7bb98cf50afbc92189d1"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

try:
    n = float(sys.argv[1])
    req = requests.get(url=url)
    j_obj = req.json()

    bitcoin_price = float(j_obj["data"]["priceUsd"])
    price = bitcoin_price * n
    print(f"${price:,.4f}")

except requests.RequestException:
    print("you sef")
except ValueError:
    sys.exit("Command-line argument is not a number")
except TypeError:
    sys.exit("Missing command-line argument")
except IndexError:
    sys.exit("Missing command-line argument")


# print(j_obj)
# print(json.dumps(j_obj, indent=2))  # just for viewing
