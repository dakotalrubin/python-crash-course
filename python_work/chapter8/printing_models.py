def print_models(unprinted_designs, completed_models):
    """Simulate printing each design until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_models(completed_models):
    """Display all completed models."""
    print("\nThe following models have been printed:")

    for model in completed_models:
        print(f"\t{model}")

# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call a function to print designs and another function to show finished models
print_models(unprinted_designs, completed_models)
show_models(completed_models)