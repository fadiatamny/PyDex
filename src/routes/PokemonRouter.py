from fastapi import APIRouter
from src.controllers import PokemonController
from src.models import Pokemon
from src.models.PokeQueryModel import PokeQuery

router = APIRouter()
controller = PokemonController()


@router.get("/{identifier}", response_model=Pokemon)
async def get(identifier: int):
    return await controller.get(identifier)


@router.get("/")
async def query_get(name: str = None, type: str = None):
    res = await controller.query(PokeQuery(name=name, type=type))
    return res['data'][0] if res['total_count'] == 1 else res


@router.post("/query")
async def query(query: PokeQuery):
    return await controller.query(query)
