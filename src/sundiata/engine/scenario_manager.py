import json
import importlib.resources
import random

def load_scenario(scenario_id: str):
    """Loads a scenario from a JSON file using importlib.resources."""
    try:
        # The 'files' function returns a Traversable object for the resource
        # We need to navigate to the 'data/events' directory within the 'sundiata' package
        # and then open the specific JSON file.
        with importlib.resources.files('sundiata.data.events').joinpath(f'{scenario_id}.json').open('r') as f:
            scenario_data = json.load(f)
        return scenario_data
    except FileNotFoundError:
        print(f"Error: Scenario file not found for ID: {scenario_id}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in scenario file for ID: {scenario_id}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading scenario {scenario_id}: {e}")
        return None

def get_all_scenario_ids() -> list[str]:
    """Returns a list of all scenario IDs from the data/events directory."""
    return [
        path.stem
        for path in importlib.resources.files("sundiata.data.events").iterdir()
        if path.is_file() and path.suffix == ".json"
    ]


def get_shuffled_scenario_ids() -> list[str]:
    """Returns a shuffled list of all scenario IDs."""
    scenario_ids = get_all_scenario_ids()
    random.shuffle(scenario_ids)
    return scenario_ids