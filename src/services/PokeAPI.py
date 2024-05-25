import requests

class PokeAPI:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"

    def get(self, name):
        url = f"{self.base_url}/pokemon/{name}"
        response = requests.get(url)
        return response.json()