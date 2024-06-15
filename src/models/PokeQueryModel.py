from pydantic import BaseModel, field_validator

from enum import Enum


class PokemonType(Enum):
    NORMAL = "normal"
    FIRE = "fire"
    WATER = "water"
    ELECTRIC = "electric"
    GRASS = "grass"
    ICE = "ice"
    FIGHTING = "fighting"
    POISON = "poison"
    GROUND = "ground"
    FLYING = "flying"
    PSYCHIC = "psychic"
    BUG = "bug"
    ROCK = "rock"
    GHOST = "ghost"
    DARK = "dark"
    DRAGON = "dragon"
    STEEL = "steel"
    FAIRY = "fairy"

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
    name: str | None = None
    type: PokemonType | None = None
    page: int = 0
    limit: int = 100

    @field_validator('type', mode="before")
    def type_validator(cls, v):
        if isinstance(v, PokemonType):
            return v

        if not isinstance(v, str):
            raise ValueError(f"Invalid Pokemon type: {v}")
        
        v = v.lower()

        if v in {e.value.lower() for e in PokemonType}:
            return PokemonType(v)
        else:
            raise ValueError(f"Invalid Pokemon type: {v}")

    __config__ = {
        "extra": "allow",
        "validate_default": True
    }
