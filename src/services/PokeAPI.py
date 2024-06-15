import json
import requests

from src.models import PokeQuery, PyDexError
from src.models.PokemonModel import Pokemon
from src.shared import CacheHandler


class PokeAPI:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"

    def _request(self, type: 'pokemon' | 'type', identifier: str):
        redis = CacheHandler.create()

        cached = redis.get(identifier)
        if (cached):
            cached = json.loads(cached)

            if (not isinstance(cached, dict)):
                cached = redis.get(cached)
                cached = json.loads(cached)

            return cached

        url = f"{self.base_url}/{type}/{identifier}"
        response = requests.get(url)
        result = response.json()

        redis.set(f'{type}_{result['name']}', result['id'])
        redis.set(f'{type}_{result['id']}', json.dumps(result))

        return result

    def _query_by_name(self, identifier: str | int):
        pokemon = self._request('pokemon', identifier)
        return pokemon

    def _query_by_type(self, type: str):
        pokeType = self._request('pokemon', type)

        response = {
            'id': pokeType['id'],
            'name': pokeType['name'],
            'pokemon': [Pokemon(id=p['pokemon']['id'], name=p['pokemon']['name']) for p in pokeType['pokemon']]
        }

        return response

    def query(self, name: str | None = None, type: str | None = None):
        if (name and type):
            raise PyDexError(
                "Invalid query. Please provide either a name or type, not both.", 400)
        if (not name and not type):
            raise PyDexError(
                "Invalid query. Please provide a name or type.", 400)

        result = None
        if (name):
            result = self._query_by_name(name)
        elif (type):
            result = self._query_by_type(type)
        else:
            raise PyDexError(
                "Invalid query. Please provide a name or type.", 400)
        
        if not isinstance(result, list):
            result = [result]
        
        response = {
            'page': 0,
            'data': result,
            'total_count': len(result)
        }

        return response

    def get(self, name: str):
        response = self.query(name=name)
        return response['data'][0]