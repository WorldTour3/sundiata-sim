from sundiata.models.player import Player
from sundiata.engine.scenario_manager import load_scenario, get_random_scenario_id
from sundiata.ui.prompts import get_choice
from sundiata.engine.resolver import resolve_choice
from sundiata.ui.screen import display_player_stats, display_scenario
from sundiata.engine.ai import insurgent_action
from sundiata.persistence.io import save_game, load_game
from sundiata.models.save import SaveGame
from rich.console import Console

console = Console()

# Define loss thresholds
MIN_BUDGET = -500
MIN_MILITARY = 0
MIN_STABILITY = 0

def game_loop(player: Player, start_turn: int):
    console.print("\nStarting game loop...")
    num_turns = 10 # Increased for more gameplay before potential loss
    for turn in range(start_turn, num_turns + 1):
        console.print(f"\n--- Turn {turn} ---")
        display_player_stats(player)

        # Load and display a random scenario
        random_scenario_id = get_random_scenario_id()
        scenario = load_scenario(random_scenario_id)
        if scenario:
            display_scenario(scenario)

            # Get player choice
            chosen_index = get_choice(scenario['choices']) - 1 # Adjust to 0-based index
            chosen_option = scenario['choices'][chosen_index]

            console.print(f"\nYou chose: {chosen_option['text']}")

            # Apply effects
            resolve_choice(player, chosen_option['effects'])

            console.print("\nPlayer Stats After Choice:")
            display_player_stats(player)

            # Insurgent AI action
            ai_message = insurgent_action(player)
            console.print(f"\n[bold yellow]Insurgent Action:[/bold yellow] {ai_message}")
            console.print("\nPlayer Stats After Insurgent Action:")
            display_player_stats(player)

            # Check for loss conditions
            if player.budget < MIN_BUDGET:
                console.print("[bold red]\nGAME OVER: Your budget has run out![/bold red]")
                break
            if player.military < MIN_MILITARY:
                console.print("[bold red]\nGAME OVER: Your military has been depleted![/bold red]")
                break
            if player.stability < MIN_STABILITY:
                console.print("[bold red]\nGAME OVER: Your country has become unstable![/bold red]")
                break

        else:
            console.print("Error loading scenario.")

        # Prompt to save game
        if console.input("[bold green]Save game? (y/n): [/bold green]").lower() == 'y':
            save_game(SaveGame(player=player, turn=turn))

    console.print("\nGame loop ended.")

def main():
    # This main function will now be called by the CLI commands
    pass