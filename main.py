from dotenv import load_dotenv
load_dotenv()

from services import PokeAPI

if __name__ == "__main__":

    poke_api = PokeAPI()
    response = poke_api.get("bulbasaur")
    response = poke_api.get(1)
