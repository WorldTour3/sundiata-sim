sundiata-sim/
├─ README.md
├─ pyproject.toml
├─ sundiata/                     # package
│  ├─ __init__.py
│  ├─ cli.py                     # Typer entry (sundiata run/new/load)
│  ├─ main.py                    # game loop orchestration
│  ├─ engine/
│  │  ├─ __init__.py
│  │  ├─ state.py                # GameState dataclass/pydantic
│  │  ├─ rules.py                # stat math, caps, decay
│  │  ├─ resolver.py             # apply choice → effects
│  │  ├─ rng.py                  # seeded RNG utilities
│  │  ├─ events.py               # load/filter events, prerequisites
│  │  ├─ operations.py           # actions (offensive, negotiate, etc.)
│  │  ├─ ai.py                   # insurgent behavior per turn
│  │  ├─ scoring.py              # win/lose & endgame summary
│  ├─ models/
│  │  ├─ country.py
│  │  ├─ forces.py
│  │  ├─ insurgency.py
│  │  ├─ event.py                # Event, Choice, Effect models
│  │  ├─ save.py                 # SaveGame schema
│  ├─ ui/
│  │  ├─ screen.py               # render dashboard (Rich tables)
│  │  ├─ prompts.py              # show options & get input
│  │  ├─ messages.py             # flavor text helpers
│  ├─ data/
│  │  ├─ config.yaml             # starting params & difficulty
│  │  ├─ regions.yaml            # region list & attributes
│  │  ├─ events/                 # dilemma packs (YAML/JSON)
│  │  │  ├─ siege_basics.yaml
│  │  │  ├─ governance.yaml
│  │  │  └─ foreign_help.yaml
│  ├─ persistence/
│  │  ├─ io.py                   # read/write saves
│  │  └─ migrations.py           # future save upgrades
│  └─ utils/
│     ├─ math.py
│     └─ logging.py
├─ saves/                        # .gitignore this
├─ tests/
│  ├─ test_state.py
│  ├─ test_events.py
│  ├─ test_resolver.py
│  └─ test_ai.py
└─ scripts/
   └─ seedcheck.py               # reproducibility tools
