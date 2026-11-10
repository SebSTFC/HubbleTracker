import requests
resp = requests.get("https://api.n2yo.com/rest/v1/satellite/positions/20580/51.57/-1.31/120/1/&apiKey=YNXLN9-L52K4G-PCRS4M-5V94")
resp.json()
