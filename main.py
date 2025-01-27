from dotenv import load_dotenv

load_dotenv()

from modules.base.router import router as base_router
from modules.pokemon.router import router as pokemon_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(base_router)
app.include_router(pokemon_router)
