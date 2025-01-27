from dotenv import load_dotenv

from modules.pokemon.repository import PokemonRepository
from resources.database import Database

load_dotenv()

from modules.pokemon.model import PokemonModel
from modules.pokemon.service import PokemonService
from modules.scraper.service import ScaperService
import os

print("[SCRAPER] Scrapping data ...")

# Get pokemon data from pokemondb.net

scraper = ScaperService(os.getenv("SCRAPER_TARGET_URL"))
response = scraper.curl()
html = scraper.parse_html(response)

# Parse HTML to get pokemon data

pokemons = []

table = html.find("table", {"id": "pokedex"})
table_body = table.find("tbody")
for index, row in enumerate(table_body.find_all("tr")):
    try:
        cells = row.find_all("td")

        types = cells[2].find_all("a")

        pokemon = PokemonModel(
            id=index + 1,
            source_id=cells[0].find("span").text,
            picture=cells[0].find("img").get("src"),
            name=cells[1].find("a").text
            + (" - " + cells[1].find("small").text if cells[1].find("small") else ""),
            ptype=(",".join([t.text for t in types])),
            total=int(cells[3].text),
            hp=int(cells[4].text),
            attack=int(cells[5].text),
            defense=int(cells[6].text),
            sp_attack=int(cells[7].text),
            sp_defense=int(cells[8].text),
            speed=int(cells[9].text),
        )

        pokemons.append(pokemon)
    except:
        pass

# Save pokemon data to database

try:
    db = Database().session()
    pokemon_repository = PokemonRepository(db)
    pokemon_service = PokemonService(repository=pokemon_repository)
    result = pokemon_service.bulk_create(pokemons)
    if result.success:
        print("[SCRAPER] Scrapping data ... DONE")
    else:
        print("[SCRAPER] Scrapping data ... ERROR")
        print(f"[SCRAPER] Error: {result.error_msg}")
except Exception as e:
    print("[SCRAPER] Scrapping data ... ERROR")
    print(f"[SCRAPER] Error: {e}")
