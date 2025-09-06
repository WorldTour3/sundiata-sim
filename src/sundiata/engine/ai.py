import random
from sundiata.models.player import Player

def insurgent_action(player: Player):
    """Simulates an action by insurgents that affects player stats, based on player's current state."""
    possible_actions = []

    # Prioritize actions based on player's weaknesses or AI's goals
    if player.stability < 30: # If stability is low, AI focuses on propaganda
        possible_actions.append({"stat": "stability", "value": -10, "message": "Insurgents intensified propaganda, further decreasing public stability."})
    elif player.military < 50: # If military is low, AI focuses on attacks
        possible_actions.append({"stat": "military", "value": -10, "message": "Insurgents launched a major offensive, severely depleting your military."})
    elif player.budget < 200: # If budget is low, AI focuses on economic disruption
        possible_actions.append({"stat": "budget", "value": -100, "message": "Insurgents disrupted trade routes, causing significant economic losses."})
    else: # General actions if no specific weakness is found
        possible_actions = [
            {"stat": "budget", "value": -50, "message": "Insurgents raided a supply convoy, reducing your budget."},
            {"stat": "military", "value": -5, "message": "Insurgents launched a surprise attack, depleting your military."},
            {"stat": "stability", "value": -5, "message": "Insurgents spread propaganda, decreasing public stability."}
        ]
    
    # If no specific action was added, fall back to general actions (shouldn't happen with the 'else' above, but for safety)
    if not possible_actions:
        possible_actions = [
            {"stat": "budget", "value": -50, "message": "Insurgents raided a supply convoy, reducing your budget."},
            {"stat": "military", "value": -5, "message": "Insurgents launched a surprise attack, depleting your military."},
            {"stat": "stability", "value": -5, "message": "Insurgents spread propaganda, decreasing public stability."}
        ]

    chosen_action = random.choice(possible_actions)
    stat_to_affect = chosen_action["stat"]
    value_to_apply = chosen_action["value"]
    message = chosen_action["message"]

    if hasattr(player, stat_to_affect):
        setattr(player, stat_to_affect, getattr(player, stat_to_affect) + value_to_apply)
        return message
    else:
        return f"Warning: Attempted to affect unknown stat: {stat_to_affect}"