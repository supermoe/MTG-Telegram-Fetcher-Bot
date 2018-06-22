import json
import requests

scryfall_base = "https://api.scryfall.com"
max_results = 4

#card_name must be a string
def fetch_card(card_name):
	print("Searching \"" + card_name + "\"")
	parameters = {"fuzzy": card_name}
	r = requests.get(scryfall_base + "/cards/named", params=parameters)
	object = r.json()
	if object['object'] == "card":
		card = {"link": object['scryfall_uri'], "name": object['name'], "img": object['image_uris']['normal']}
		print("-> Found " + card['name'])
		return {"success": 0, "card":card}
	elif object['object'] == "error":
		print("-> " + object['details'])
		print(object)
		if 'type' in object and object['type'] == 'ambiguous':
			print("--> searching for possible cards")
			return search_card(card_name)
		return {"success": -1, "details":object['details']}
	else:
		print("-> Unknown Error")
		return {"success": -1, "details":"Unknown Error."}

def search_card(card_name):
	parameters = {"q": card_name, "order": "released", "include_extras":False}
	r = requests.get(scryfall_base + "/cards/search", params=parameters)
	object = r.json()
	if object['object'] == "list":
		print("---> Found " + str(len(object['data'])) + " cards:")
		object['data'] = object['data'][:max_results]
		cards = []
		for card in object['data']:
			print("----> " + card['name'])
			cards.append(card['name'])
		return {"success": 1, "query":card_name, "list":cards}
	elif object['object'] == "error":
		print("---> " + object['details'])
		return {"success": -1, "details":object['details']}
	else:
		print("---> Unknown Error")
		return {"success": -1, "details":"Unknown Error."}
	

	