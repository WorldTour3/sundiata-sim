from rich.console import Console
from rich.table import Table
from sundiata.models.player import Player

console = Console()

def display_player_stats(player: Player):
    """Displays the player's current stats using a Rich Table."""
    table = Table(title="Player Stats")
    table.add_column("Stat", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Budget", str(player.budget))
    table.add_row("Military", str(player.military))
    table.add_row("Stability", str(player.stability))

    console.print(table)

def display_scenario(scenario: dict):
    """Displays the scenario title, description, and choices using Rich."""
    console.print(f"[bold blue]Scenario: {scenario['title']}[/bold blue]")
    console.print(f"[italic]{scenario['description']}[/italic]")

    console.print("\n[bold green]Choices:[/bold green]")
    for i, choice in enumerate(scenario['choices']):
        console.print(f"{i + 1}. {choice['text']}")
