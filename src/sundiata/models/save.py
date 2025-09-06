from dataclasses import dataclass
from sundiata.models.player import Player

@dataclass
class SaveGame:
    player: Player
    turn: int
