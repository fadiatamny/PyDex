import json
import requests

from src.models import PokeQuery
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
    
    def query(self, query: PokeQuery):
        pass
