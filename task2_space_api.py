import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    # process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()