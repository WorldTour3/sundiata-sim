import json
from pathlib import Path
import random

def load_scenario(scenario_id: str):
    """Loads a scenario from a JSON file."""
    file_path = Path(__file__).parent.parent.parent / "data" / "events" / f"{scenario_id}.json"
    try:
        with open(file_path, 'r') as f:
            scenario_data = json.load(f)
        return scenario_data
    except FileNotFoundError:
        print(f"Error: Scenario file not found for ID: {scenario_id}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in scenario file for ID: {scenario_id}")
        return None

def get_random_scenario_id() -> str:
    """Returns the ID of a randomly selected scenario."""
    scenario_files = ["siege_basics", "governance", "foreign_help"]
    return random.choice(scenario_files)