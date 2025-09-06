class Player:
    def __init__(self, budget: int = 1000, military: int = 100, stability: int = 50):
        self.budget = budget
        self.military = military
        self.stability = stability

    def __str__(self):
        return f"Budget: {self.budget}, Military: {self.military}, Stability: {self.stability}"
