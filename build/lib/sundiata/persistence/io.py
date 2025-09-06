import json
from pathlib import Path
from sundiata.models.save import SaveGame
from sundiata.models.player import Player
from json import JSONEncoder

class SaveGameEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Player):
            return obj.__dict__
        return JSONEncoder.default(self, obj)

def save_game(save_game: SaveGame, filename: str = "sundiata_save.json"):
    """Saves the game state to a JSON file."""
    save_path = Path("saves") / filename
    save_path.parent.mkdir(parents=True, exist_ok=True) # Ensure 'saves' directory exists
    with open(save_path, 'w') as f:
        json.dump(save_game.__dict__, f, indent=4, cls=SaveGameEncoder)
    print(f"Game saved to {save_path}")

def load_game(filename: str = "sundiata_save.json") -> SaveGame | None:
    """Loads the game state from a JSON file."""
    save_path = Path("saves") / filename
    if not save_path.exists():
        print(f"No save game found at {save_path}")
        return None
    try:
        with open(save_path, 'r') as f:
            data = json.load(f)
        player_data = data.get("player", {})
        player = Player(**player_data)
        turn = data.get("turn", 0)
        return SaveGame(player=player, turn=turn)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in save file: {save_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading game: {e}")
        return None
