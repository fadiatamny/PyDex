from src.models import PokeQuery, PyDexError
from src.services import PokeAPI


class PokemonController:
    def __init__(self):
        self.service = PokeAPI()

    async def get(self, identifier: str | int):
        return self.service.get(identifier)

    async def query(self, query: PokeQuery):
        if not query.type and not query.name:
            raise PyDexError(
                "At least one of 'type' or 'name' must be provided.", 400)
        if query.type and query.name:
            raise PyDexError(
                "Only one of 'type' or 'name' can be provided.", 400)
        return self.service.query(name=query.name, type=query.type)
