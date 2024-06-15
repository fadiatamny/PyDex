from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str

    __config__ = {
        "extra": "allow",
        "validate_default": True
    }

class APIPokemon(Pokemon):
    id: int
    name: str
    type: str

    __config__ = {
        "validate_default": True
    }
