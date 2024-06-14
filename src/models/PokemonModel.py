from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str

    class Config:
        extra = "allow"
        validate_all = True
    
