from src.models import PokeQuery, PyDexError
from src.services import PokeAPI


class PokemonController:
    def __init__(self):
        self.service = PokeAPI()

    async def get(self, identifier: str | int):
        return self.service.get(identifier)

    async def query(self, query: PokeQuery):
        return self.service.query(query=query)
