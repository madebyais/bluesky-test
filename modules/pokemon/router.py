from fastapi import APIRouter, Depends, Query
from modules.pokemon.service import PokemonService
from modules.pokemon.middleware import get_pokemon_service


router = APIRouter(prefix="/api/v1/pokemon", tags=["pokemon"])


@router.get("")
def get_all_pokemon(
    service: PokemonService = Depends(get_pokemon_service),
    limit: int = Query(default=10, ge=1, le=100),
    skip: int = Query(default=0, ge=0),
):
    try:
        result = service.get_all(limit=limit, skip=skip)
        if not result.success:
            return {"success": False, "message": result.error_msg}

        return {"data": result.data}
    except Exception as e:
        return {"success": False, "message": str(e)}
