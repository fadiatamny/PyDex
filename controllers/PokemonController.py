from services import PokeAPI

class PokemonController:
    def __init__(self):
        self.service = PokeAPI()

    async def get(self, identifier: str | int):
        return self.service.get(identifier)