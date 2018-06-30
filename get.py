import json
import requests

scryfall_base = "https://api.scryfall.com"
max_results = 20

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
		return {"success": -1, "details":object['details']}
	else:
		print("-> Unknown Error")
		return {"success": -1, "details":"Unknown Error."}

def fetch_inline(name):
	print("Inline search for \"" + name + "\"")
	parameters = {"q": name, "order": "released", "include_extras":False}
	r = requests.get(scryfall_base + "/cards/search", params=parameters)
	object = r.json()
	if object['object'] == "list":
		cards = []
		print("-> Found " + str(len(object['data'])) + " cards:")
		for card in object['data']:
			if 'image_uris' in card:
				print("--> " + card['name'])
				cards.append({'name':card['name'], 'thumb':card['image_uris']['small'], 'full':card['image_uris']['normal'], 'url':card['scryfall_uri']})
			else:
				print("--> " + card['name'])
				for face in card['card_faces']:
					cards.append({'name':face['name'], 'thumb':face['image_uris']['small'], 'full':face['image_uris']['normal'], 'url':card['scryfall_uri']})
		return cards[:max_results]
	else:
		print('-> Error')
		return []


	

	