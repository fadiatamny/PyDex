from unittest import TestCase
from unittest.mock import patch, MagicMock
import json
from pytest import MonkeyPatch
import pytest
from src.models.PokeQueryModel import PokeQuery
from src.services import PokeAPI
from src.shared import Config


class TestPokeAPI(TestCase):
    def setUp(self):
        self.monkeypatch = MonkeyPatch()

    @patch('src.shared.CacheHandler.create')
    @patch('requests.get')
    def test_get_pokemon_cached(self, mock_requests_get, mock_cache_create):
        self.monkeypatch.setenv("DISABLE_CACHE", "false")

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

    @patch('src.shared.CacheHandler.create')
    @patch('requests.get')
    def test_get_pokemon_not_cached(self, mock_requests_get, mock_cache_create):
        self.monkeypatch.setenv("DISABLE_CACHE", "false")
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
        mock_cache_handler.set.assert_any_call('pokemon_bulbasaur', 1)
        mock_cache_handler.set.assert_any_call(
            'pokemon_1', json.dumps(response_data))
        mock_requests_get.assert_called_once_with(
            'https://pokeapi.co/api/v2/pokemon/bulbasaur')

    @patch('requests.get')
    def test_query_pokemon_by_name(self, mock_requests_get):
        self.monkeypatch.setenv("DISABLE_CACHE", "true")
        response_data = {
            'id': 1,
            'name': 'bulbasaur',
            'type': 'grass'
        }
        mock_response = MagicMock()
        mock_response.json.return_value = response_data
        mock_requests_get.return_value = mock_response

        api = PokeAPI()
        _ = api.query(PokeQuery(**{'name': 'bulbasaur'}))
        mock_requests_get.assert_called_once_with(
            'https://pokeapi.co/api/v2/pokemon/bulbasaur')

    @patch('requests.get')
    def test_query_pokemon_by_type(self, mock_requests_get):
        self.monkeypatch.setenv("DISABLE_CACHE", "true")
        response_data = {
            'id': 12,
            'name': 'grass'
        }
        mock_response = MagicMock()
        mock_response.json.return_value = response_data
        mock_requests_get.return_value = mock_response

        api = PokeAPI()
        _ = api.query(PokeQuery(**{'type': 'gRass'}))
        mock_requests_get.assert_called_once_with(
            'https://pokeapi.co/api/v2/type/grass')
