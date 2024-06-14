from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str

    __config__ = {
        "extra": "allow",
        "validate_default": True
    }