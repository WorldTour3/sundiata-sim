def get_choice(options: list) -> int:
    """Prompts the user to choose from a list of options and returns the 1-based index of the choice."""
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a number within the given range.")
        except ValueError:
            print("Invalid input. Please enter a number.")
