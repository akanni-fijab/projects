import os
import dotenv
import requests
import sys

dotenv.load_dotenv()  # Load envars
if os.getenv("api_key") is None:
    sys.exit("Empty api str")


api = os.getenv("api_key")  # store api key form .env file

crypto = [
    "bitcoin",
    "bitcoin-cash",
    "tether",
    "ethereum",
    "dogecoin",
    "solana",
    "toncoin",
    "monero",
]


def get_price():
    for i in range(len(crypto)):
        print(f"{i}. {crypto[i]}")
    try:
        choice = int(input("Enter an index: "))
        n = int(input("Enter an amount: "))

        url = f"https://rest.coincap.io/v3/assets/{crypto[choice]}?apiKey={api}"
        req = requests.get(url=url)
        json_obj = req.json()  # store req as a json object for easy indexing
        # print(json_obj)
        # print(json.dumps(json_obj, indent=2))  # just for viewing

        crypto_price = float(json_obj["data"]["priceUsd"])
        price = crypto_price * n
        print(f"${price:,.2f}")

    except ValueError:
        print("invalid input 🗿")
    except IndexError:
        print("index is out of bounds 🫵")
    except requests.RequestException:
        print("Most likely a network issue 😦")
