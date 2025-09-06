import sys
from pathlib import Path

# Add the src directory to sys.path for local development
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import typer
from sundiata.main import game_loop
from sundiata.models.player import Player
from sundiata.persistence.io import load_game
from rich.console import Console

console = Console()

app = typer.Typer()

@app.command()
def new():
    """Start a new game."""
    console.print("Starting a new game...")
    player = Player()
    game_loop(player, 1)

@app.command()
def load():
    """Load a saved game."""
    console.print("Loading game...")
    loaded_game = load_game()
    if loaded_game:
        game_loop(loaded_game.player, loaded_game.turn + 1) # Start from next turn
    else:
        console.print("[bold red]No saved game found.[/bold red]")

def _entry_point():
    app()

if __name__ == "__main__":
    _entry_point()