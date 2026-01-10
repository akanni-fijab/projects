import requests


def main():
    page = 1
    limit = 100
    querry = input("Enter an artist: ")
    #Gives us artworks by a particular artist

    url = f"https://api.artic.edu/api/v1/artworks/search?page={page}&limit={limit}"
    # header = {"User-Agent": "Mozzila/5.0"}
    try:
        req = requests.get(url, querry)
        req.raise_for_status()
        obj = req.json()

    except requests.HTTPError:
        print("Connection issue")
        return  # it is a function so it exits on errors "return"

    for artwork in obj["data"]:
        print(f"* {artwork['title']}")


main()
