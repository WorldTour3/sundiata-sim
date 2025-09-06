# Sundiata Sim

A turn-based command-line strategy game where the player takes the role of a head of state in a fictional country facing insurgency and governance challenges.

## 🎯 Goal

Simulate tough leadership decisions (military, diplomacy, governance).
Each turn presents a scenario (e.g., siege, economic crisis, rebellion).
Player chooses from options with different trade-offs.
Game tracks resources, military strength, public support, and stability.
Outcomes evolve dynamically, influenced by player decisions and random events.

## 🛠️ Tech & Setup

Built in Python (CLI only).
Runs in VS Code terminal or similar command-line environments.
Structured into modular components (engine, player, scenarios, data).
JSON used for scenario and option definitions (easy to expand).

## 📂 Key Components

- `src/sundiata/main.py`: Orchestrates the main game loop.
- `src/sundiata/cli.py`: Command-line interface for starting new games or loading saved ones.
- `src/sundiata/engine/`: Contains core game logic, including scenario management, AI, and outcome resolution.
- `src/sundiata/models/`: Defines data structures for game entities like Player, SaveGame, etc.
- `src/sundiata/data/`: Stores game configuration and scenario definitions (JSON files).
- `src/sundiata/ui/`: Handles user interface elements, including displaying stats and scenarios.
- `src/sundiata/persistence/`: Manages saving and loading game progress.

## 🚀 Getting Started

To get the Sundiata Sim game up and running on your local machine, follow these steps:

### 1. Clone the Repository

First, clone the project repository to your local machine using Git:

```bash
git clone https://github.com/WorldTour3/sundiata-sim.git
cd sundiata-sim
```

### 2. Install Dependencies

Navigate to the project's root directory and install the required Python packages. It's recommended to use a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -e .
```

This command installs the project in editable mode, making the `sundiata` command available in your terminal.

## 🎮 How to Play

Once the setup is complete, you can start playing Sundiata Sim:

### Start a New Game

To begin a new game from the start:

```bash
./sundiata new
```

### Load a Saved Game

To continue a previously saved game:

```bash
./sundiata load
```

### Gameplay

- The game is turn-based. Each turn, you will be presented with a scenario.
- Read the scenario description and the available choices.
- Enter the number corresponding to your chosen option when prompted.
- Your decisions will affect your country's budget, military strength, and stability.
- Insurgent AI will also take actions that impact your stats.
- The game ends if your budget, military, or stability fall below critical thresholds (Game Over).
- Survive all turns without losing to win the game!

Enjoy leading your country!