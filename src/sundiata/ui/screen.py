from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from sundiata.models.player import Player

console = Console()


def display_scenario(scenario: dict, messages: list[str] = None):
    """Displays the scenario title, description, and choices using Rich."""
    if messages:
        for message in messages:
            console.print(message)

    console.print(f"[bold blue]Scenario: {scenario['title']}[/bold blue]")
    console.print(f"[italic]{scenario['description']}[/italic]")

    console.print("\n[bold green]Choices:[/bold green]")
    for i, choice in enumerate(scenario['choices']):
        console.print(f"{i + 1}. {choice['text']}")

def display_game_end_screen(player: Player, message: str, status: str):
    """Displays the game over or win screen with final stats."""
    panel_title = "[bold white on red]GAME OVER[/bold white on red]" if status == "lose" else "[bold white on green]VICTORY![/bold white on green]"
    panel_content = f"[bold]{message}[/bold]\n\nFinal Stats:"

    final_stats_table = Table.grid()
    final_stats_table.add_column(style="cyan")
    final_stats_table.add_column(style="magenta")
    final_stats_table.add_row("Budget", str(player.budget))
    final_stats_table.add_row("Military", str(player.military))
    final_stats_table.add_row("Stability", str(player.stability))

    console.print(Panel(panel_content, title=panel_title, expand=False))
    console.print(final_stats_table)