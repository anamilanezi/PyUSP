# If a default value is defined, the corresponding argument can be excluded in the function call

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name="Muffin")
describe_pet(pet_name="Leslie", animal_type="cat")