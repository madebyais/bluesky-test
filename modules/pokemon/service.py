from typing import List
from modules.pokemon.repository import PokemonRepository
from modules.base.model import ServiceResultModel
from modules.pokemon.model import PokemonModel


class PokemonService:
    def __init__(self, repository: PokemonRepository):
        self.repository = repository

    def get_all(self, limit: int = 10, skip: int = 0):
        try:
            result = self.repository.find_all(limit=limit, skip=skip)
            return ServiceResultModel(
                success=True,
                data=result.data,
            )
        except Exception as e:
            return ServiceResultModel(
                error_msg=str(e),
            )

    def bulk_create(self, data: List[PokemonModel]):
        try:
            for item in data:
                self.repository.insert(item)

            return ServiceResultModel(
                success=True,
                message="Succesfully insert pokemon data.",
                data=data,
            )
        except Exception as e:
            return ServiceResultModel(
                error_msg=str(e),
            )
