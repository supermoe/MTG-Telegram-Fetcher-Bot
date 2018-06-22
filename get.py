import json
import requests

scryfall_base = "https://api.scryfall.com"

#card_name must be a string
def fetch_card(card_name):
	print("Searching \"" + card_name + "\"")
	parameters = {"fuzzy": card_name}
	r = requests.get(scryfall_base + "/cards/named", params=parameters)
	object = r.json()
	if object['object'] == "card":
		print("-> Found")
		card = {"link": object['scryfall_uri'], "name": object['name'], "img": object['image_uris']['normal']}
		return {"success": True, "card":card}
	elif object['object'] == "error":
		print("-> " + object['details'])
		return {"success": False, "details":object['details']}
	else:
		return {"success": False, "details":"Unknown Error"}
	