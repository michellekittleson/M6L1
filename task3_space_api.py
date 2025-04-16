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


def find_heaviest_planet():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    bodies = response.json()['bodies']

    heaviest_name = None
    heaviest_mass = 0

    for body in bodies:
        if body.get('isPlanet') and body.get('mass'):
            m = body['mass']
            mass_kg = m['massValue'] * 10 **m['massExponent']
            if mass_kg > heaviest_mass:
                heaviest_mass = mass_kg
                heaviest_name = body.get('englishName', body.get('name'))
    
    return heaviest_name, heaviest_mass

name, mass = find_heaviest_planet()
print(f"The heaviest planet is {name} has a mass of {mass:.2e} kg.")




