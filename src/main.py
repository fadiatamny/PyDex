from services import PokeAPI

if __name__ == "__main__":

    poke_api = PokeAPI()
    response = poke_api.get("pikachu")
    # response = poke_api.get(1)
    from pprint import pprint
    pprint(response['name'])
