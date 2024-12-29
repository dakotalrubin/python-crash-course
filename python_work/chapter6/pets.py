pet_0 = {
    'name': 'abbey',
    'animal': 'dog',
    'type': 'golden retriever',
    'owner': 'dakota'
}

pet_1 = {
    'name': 'daisy',
    'animal': 'dog',
    'type': 'mixed',
    'owner': 'dylan'
}

pet_2 = {
    'name': 'fluff',
    'animal': 'chinchilla',
    'type': 'short-tailed',
    'owner': 'steve'
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"Name: {pet['name'].title()}")
    print(f"Animal: {pet['animal'].title()}")
    print(f"Type: {pet['type'].title()}")
    print(f"Owner: {pet['owner'].title()}\n")