from sundiata.models.player import Player
from sundiata.engine.scenario_manager import load_scenario, get_shuffled_scenario_ids
from sundiata.ui.prompts import get_choice
from sundiata.engine.resolver import resolve_choice
from sundiata.ui.screen import display_player_stats, display_scenario, display_game_end_screen
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
    game_over = False
    current_turn = start_turn
    game_end_message = ""
    game_end_status = ""

    # Get a shuffled list of scenario IDs
    shuffled_scenario_ids = get_shuffled_scenario_ids()

    for turn in range(start_turn, num_turns + 1):
        current_turn = turn
        console.print(f"\n--- Turn {turn} --- ")
        display_player_stats(player)

        # If we've run out of scenarios, reshuffle and start over
        if not shuffled_scenario_ids:
            shuffled_scenario_ids = get_shuffled_scenario_ids()

        # Load and display a scenario from our shuffled list
        scenario_id = shuffled_scenario_ids.pop(0)
        scenario = load_scenario(scenario_id)
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
                game_end_message = "Your budget has run out!"
                game_end_status = "lose"
                game_over = True
                break
            if player.military < MIN_MILITARY:
                game_end_message = "Your military has been depleted!"
                game_end_status = "lose"
                game_over = True
                break
            if player.stability < MIN_STABILITY:
                game_end_message = "Your country has become unstable!"
                game_end_status = "lose"
                game_over = True
                break

        else:
            console.print("Error loading scenario.")

    if not game_over:
        game_end_message = "You have successfully led your country!"
        game_end_status = "win"

    # Display game end screen
    display_game_end_screen(player, game_end_message, game_end_status)

    # Automatic save at the end of the game loop (win or lose)
    save_game(SaveGame(player=player, turn=current_turn))
    console.print("\nGame loop ended.")

def main():
    # This main function will now be called by the CLI commands
    pass
