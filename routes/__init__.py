from fastapi import APIRouter
from .pokemon_router import router as PokeRouter

routes = APIRouter()

routes.include_router(PokeRouter, prefix="/pokemon", tags=["pokemon"])


__all__ = ['routes']