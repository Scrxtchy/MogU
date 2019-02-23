import requests
from time import sleep

key = "" #https://xivapi.com/app

x = requests.get("https://www.garlandtools.org/db/doc/item/en/3/24988.json").json()

for item in range(23768, 23783):
	y = requests.get("https://xivapi.com/market/cactuar/items/{0}?key={1}".format(str(item), key)).json()
	for z in y['Prices']:
		if z['IsHQ']:
			print(y['Item']['Name'] + ": {}".format(z['PricePerUnit']) )
			break
sleep(0.5)
