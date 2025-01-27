from fastapi import Depends
from modules.pokemon.repository import PokemonRepository
from modules.pokemon.service import PokemonService
from resources.database import get_db
from sqlite3 import Connection


def get_pokemon_service(db: Connection = Depends(get_db)):
    repository = PokemonRepository(db)
    return PokemonService(repository)
