import requests
from time import sleep

key = "" #https://xivapi.com/app
items = [19935, 19960, 19961, 19992, 20005, 22416, 22412, 22413, 22414, 22421, 22415, 21279, 22475, 22477, 23382, 24244, 24245, 24246, 24247, 24248, 24249]
costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1600, 1600, 1600, 50, 20, 20, 20, 20, 20, 20]
for idx, item in enumerate(items):
	x = requests.get("https://xivapi.com/market/cactuar/items/{0}?key={1}".format(str(item), key)).json()
	print(x['Item']['Name'] + " NQ: {} HQ: {}".format(costs[idx], int(costs[idx] * 2.5)))
	for p in x['Prices']:
		pr = (p['PricePerUnit'] / float(str(costs[idx])[:-1]))
		if p['IsHQ']:
			pr = pr / 2.5
		print("ppu: {} {}".format(pr, "O" if p['IsHQ'] else "X"))
	sleep(0.5)
