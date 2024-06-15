import json
import requests

from src.models import PokeQuery, PyDexError
from src.shared import CacheHandler

class PokeAPI:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"

    def get(self, identifier: str | int):
        redis = CacheHandler.create()

        cached = redis.get(identifier)
        if (cached):
            cached = json.loads(cached)

            if (not isinstance(cached, dict)):
                cached = redis.get(cached)
                cached = json.loads(cached)

            return cached
        
        url = f"{self.base_url}/pokemon/{identifier}"
        response = requests.get(url)
        pokemon = response.json()


        redis.set(pokemon['name'], pokemon['id'])
        redis.set(pokemon['id'], json.dumps(pokemon))

        return pokemon
    
    def _query_by_name(self, name: str):
        url = f"{self.base_url}/pokemon/{name}"
        response = requests.get(url)
        pokemon = response.json()
        return pokemon
    
    def _query_by_type(self, type: str):
        url = f"{self.base_url}/type/{type}"
        response = requests.get(url)
        pokemon = response.json()
        return pokemon

    def query(self, query: PokeQuery):
        if (query.name):
            return self._query_by_name(query.name)
        elif (query.type):
            return self._query_by_type(query.type.value)
        else:
            raise PyDexError("Invalid query. Please provide a name or type.", 400)
