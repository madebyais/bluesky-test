from typing import Optional
from pydantic import BaseModel


class PokemonModel(BaseModel):
    id: int
    source_id: str
    picture: Optional[str]
    name: str
    ptype: Optional[str]
    total: Optional[int]
    hp: Optional[int]
    attack: Optional[int]
    defense: Optional[int]
    sp_attack: Optional[int]
    sp_defense: Optional[int]
    speed: Optional[int]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data[0],
            source_id=data[1],
            picture=data[2],
            name=data[3],
            ptype=data[4],
            total=data[5],
            hp=data[6],
            attack=data[7],
            defense=data[8],
            sp_attack=data[9],
            sp_defense=data[10],
            speed=data[11],
        )

    def to_dict(self):
        return (
            self.id,
            self.source_id,
            self.picture,
            self.name,
            self.ptype,
            self.total,
            self.hp,
            self.attack,
            self.defense,
            self.sp_attack,
            self.sp_defense,
            self.speed,
        )
