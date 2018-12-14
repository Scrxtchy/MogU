import requests
from pprint import pprint
from time import sleep
from beautifultable import BeautifulTable
table = BeautifulTable()
x = requests.get('https://www.garlandtools.org/db/doc/item/en/3/10307.json').json()
table.column_headers = ["Name", "CSeals", "Gseals"]

def check(price, id):
	e = requests.get('https://www.garlandtools.org/db/doc/item/en/3/{}.json'.format(item['item'][0]['id'])).json()['item']
	if 'delivery' in e:
		table.append_row([e['name'], int(price), int(round(e['delivery'] / int(price)))])

for l in x['item']['tradeCurrency']:
	if l['shop'] in ['Exchange Centurio Seals', 'Exchange Centurio Seals (Advanced)', 'Centurio Seal Exchange I', 'Centurio Seal Exchange II']:
		continue
	
	for item in l['listings']:
		check(item['currency'][0]['amount'], item['item'][0]['id'])
table.column_alignments['Name'] = BeautifulTable.ALIGN_LEFT
table.sort("Gseals")
print(table)		
