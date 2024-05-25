from unittest import TestCase
from unittest.mock import patch, MagicMock
import json
from ...services import PokeAPI

class TestPokeAPI(TestCase):

    @patch('shared.CacheHandler.create')
    @patch('requests.get')
    def test_get_pokemon_cached(self, mock_requests_get, mock_cache_create):
        mock_cache_handler = MagicMock()
        mock_cache_create.return_value = mock_cache_handler

        cached_pokemon = {
            'id': 1,
            'name': 'bulbasaur',
            'type': 'grass'
        }
        mock_cache_handler.get.return_value = json.dumps(cached_pokemon)

        api = PokeAPI()
        result = api.get('bulbasaur')

        self.assertEqual(result, cached_pokemon)
        mock_requests_get.assert_not_called()

    @patch('shared.CacheHandler.create')
    @patch('requests.get')
    def test_get_pokemon_not_cached(self, mock_requests_get, mock_cache_create):
        mock_cache_handler = MagicMock()
        mock_cache_create.return_value = mock_cache_handler

        response_data = {
            'id': 1,
            'name': 'bulbasaur',
            'type': 'grass'
        }
        mock_response = MagicMock()
        mock_response.json.return_value = response_data
        mock_requests_get.return_value = mock_response

        mock_cache_handler.get.side_effect = [None, json.dumps(response_data)]

        api = PokeAPI()
        result = api.get('bulbasaur')

        self.assertEqual(result, response_data)
        mock_cache_handler.set.assert_any_call('bulbasaur', 1)
        mock_cache_handler.set.assert_any_call(1, json.dumps(response_data))
        mock_requests_get.assert_called_once_with('https://pokeapi.co/api/v2/pokemon/bulbasaur')
