from fastapi import APIRouter
from controllers import PokemonController
from models import Pokemon

router = APIRouter()
controller = PokemonController()

@router.get("/{identifier}", response_model=Pokemon)
async def get(identifier: int):
    return await controller.get(identifier)