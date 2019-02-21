import requests
from time import sleep

key = "" #https://xivapi.com/app

x = requests.get("https://www.garlandtools.org/db/doc/item/en/3/24988.json").json()

for item in x['item']['tradeShops'][0]['listings']:
	y = requests.get("https://xivapi.com/market/cactuar/items/{0}?key={1}".format(str(item['currency'][0]['id']), key)).json()
	print(item['currency'][0]['id'] + "cost: {}".format(y['Prices'][0]['PricePerUnit']) )
sleep(0.5)
