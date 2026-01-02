import requests
import sys
import json

# r = requests.get("http://itunes.apple.com/search?entity=song&limit=1&term=rema")
# Attmpting to obtain artist info from itunes

# JavaScript Object notation JSON
#
#
#
if len(sys.argv) != 2:  # exit if usert does not enter a cmdline flag
    sys.exit()
limit: int = 10  # easy modification of queries

song_req = requests.get(
    f"http://itunes.apple.com/search?entity=song&limit={limit}&term=" + sys.argv[1]
)

print(json.dumps(song_req.json(), indent=2))  # human readable fotmat


obj = song_req.json()  # store the request as a json Object

for result in obj["results"]:
    print(result["trackName"])  # imagin result equal value so dict_name["key"] == value
