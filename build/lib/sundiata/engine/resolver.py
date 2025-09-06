from sundiata.models.player import Player

def resolve_choice(player: Player, choice_effects: dict):
    """Applies the effects of a chosen option to the player's stats."""
    for stat, value in choice_effects.items():
        if hasattr(player, stat):
            setattr(player, stat, getattr(player, stat) + value)
        else:
            print(f"Warning: Player does not have stat: {stat}")
