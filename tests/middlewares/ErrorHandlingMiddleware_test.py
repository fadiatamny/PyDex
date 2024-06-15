from unittest import TestCase
from unittest.mock import patch
from fastapi.testclient import TestClient
from pytest import MonkeyPatch
from src.app import app
from src.models import PyDexError

client = TestClient(app)
class TestPokeAPI(TestCase):
    def setUp(self):
        self.monkeypatch = MonkeyPatch()

    @patch("src.services.PokeAPI.get")
    def test_get_pokemon_failure(self, mock_get_pokemon):
        self.monkeypatch.setenv("DISABLE_CACHE", "false")
        mock_get_pokemon.side_effect = PyDexError("Pokémon service is unavailable.", 503)
        response = client.get("/pokemon/25")
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json(), {"detail": "Pokémon service is unavailable."})

