from src.models import PokeQuery
from src.services import PokeAPI

class PokemonController:
    def __init__(self):
        self.service = PokeAPI()

    async def get(self, identifier: str | int):
        return self.service.get(identifier)
    
    async def query(self, query: PokeQuery): 
        if not query.type and not query.name:
            raise ValueError("At least one of 'type' or 'name' must be provided.")
        return self.service.query(query)