import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    print("Planets:")
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']
            orbit_period = planet['sideralOrbit']

            print(f"{name}")

fetch_planet_data()


def find_heaviest_planet(planets):
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    

    for planet in planets:
        planet_masses = []
        if planet['isPlanet']:
            planet_masses.append(planet['mass'])
    
    max_mass = max(planet_masses)
    return max_mass

print(f"The heaviest planet is {name} has a mass of {find_heaviest_planet(planets)} kg.")




