import random
from sundiata.models.player import Player

def insurgent_action(player: Player):
    """Simulates a random action by insurgents that affects player stats."""
    actions = [
        {"stat": "budget", "value": -50, "message": "Insurgents raided a supply convoy, reducing your budget."},
        {"stat": "military", "value": -5, "message": "Insurgents launched a surprise attack, depleting your military."},
        {"stat": "stability", "value": -5, "message": "Insurgents spread propaganda, decreasing public stability."}
    ]
    
    chosen_action = random.choice(actions)
    stat_to_affect = chosen_action["stat"]
    value_to_apply = chosen_action["value"]
    message = chosen_action["message"]

    if hasattr(player, stat_to_affect):
        setattr(player, stat_to_affect, getattr(player, stat_to_affect) + value_to_apply)
        return message
    else:
        return f"Warning: Attempted to affect unknown stat: {stat_to_affect}"
