import sqlite3
from modules.pokemon.model import PokemonModel
from modules.base.model import RepositoryResultModel


class PokemonRepository:

    def __init__(self, db: sqlite3.Connection = None) -> None:
        self.db = db

    def find_all(self, limit: int = 10, skip: int = 0, is_all: bool = False) -> dict:
        try:
            if not is_all:
                data = self.db.execute(
                    "SELECT * FROM pokemon LIMIT ? OFFSET ?", (limit, skip)
                ).fetchall()
            else:
                data = self.db.execute("SELECT * FROM pokemon").fetchall()

            pokemon_data = []
            for item in data:
                pokemon_data.append(PokemonModel.from_dict(data=item))

            return RepositoryResultModel(data=pokemon_data)
        except sqlite3.Error as e:
            raise Exception(f"Failed to fetch pokemon data detail={str(e)}")

    def insert(self, data: PokemonModel) -> PokemonModel:
        try:
            self.db.execute(
                "INSERT INTO pokemon (id, source_id, picture, name, ptype, total, hp, attack, defense, sp_attack, sp_defense, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                data.to_dict(),
            )
            self.db.commit()

            return RepositoryResultModel(data=data)
        except sqlite3.Error as e:
            raise Exception(
                f"Failed to insert pokemon data source_id={data.source_id} detail={str(e)}"
            )

    def delete(self, id: int) -> dict:
        try:
            self.db.execute("DELETE FROM pokemon WHERE id=?", (id,))
            self.db.commit()

            return RepositoryResultModel(data=id)
        except sqlite3.Error as e:
            raise Exception(f"Failed to delete pokemon data id={id} detail={str(e)}")
