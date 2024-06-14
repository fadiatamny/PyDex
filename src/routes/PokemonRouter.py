from fastapi import APIRouter
from src.controllers import PokemonController
from src.models import Pokemon

router = APIRouter()
controller = PokemonController()

@router.get("/{identifier}", response_model=Pokemon)
async def get(identifier: int):
    return await controller.get(identifier)