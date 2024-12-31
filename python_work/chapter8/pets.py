def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('willie')