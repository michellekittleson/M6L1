import requests
import json

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    json_data = response.text

    pokemon_data = json.loads(json_data)

    return pokemon_data["weight"]

def calculate_average_weight():
    pikachu_weight = fetch_pokemon_data("pikachu")
    bulbasaur_weight = fetch_pokemon_data("bulbasaur")
    charmander_weight = fetch_pokemon_data("charmander")

    weight_sum = pikachu_weight + bulbasaur_weight + charmander_weight
    average_weight = weight_sum / 3

    print(f"Average weight: {average_weight}")

calculate_average_weight()

