from pydantic import BaseModel

from enum import Enum


class PokemonType(Enum):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    ELECTRIC = "Electric"
    GRASS = "Grass"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DARK = "Dark"
    DRAGON = "Dragon"
    STEEL = "Steel"
    FAIRY = "Fairy"

    @staticmethod
    def from_number(number):
        mapping = {
            0: PokemonType.NORMAL,
            1: PokemonType.FIRE,
            2: PokemonType.WATER,
            3: PokemonType.ELECTRIC,
            4: PokemonType.GRASS,
            5: PokemonType.ICE,
            6: PokemonType.FIGHTING,
            7: PokemonType.POISON,
            8: PokemonType.GROUND,
            9: PokemonType.FLYING,
            10: PokemonType.PSYCHIC,
            11: PokemonType.BUG,
            12: PokemonType.ROCK,
            13: PokemonType.GHOST,
            14: PokemonType.DARK,
            15: PokemonType.DRAGON,
            16: PokemonType.STEEL,
            17: PokemonType.FAIRY
        }
        return mapping.get(number, None)


class PokeQuery(BaseModel):
    name: str | None
    type: PokemonType
    limit: int
    offset: int

    __config__ = {
        "extra": "allow",
        "validate_default": True
    }
