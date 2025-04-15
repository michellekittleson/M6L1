import requests
import json

def fetch_name_abilities_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    json_data = response.text

    pikachu_data = json.loads(json_data)

    print(pikachu_data["name"])
    print(pikachu_data["abilities"])

fetch_name_abilities_pokemon()