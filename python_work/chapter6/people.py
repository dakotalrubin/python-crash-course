person_0 = {
    'first': 'eren',
    'last': 'yeager',
    'age': 19,
    'city': 'shiganshina'
}

person_1 = {
    'first': 'reiner',
    'last': 'braun',
    'age': 24,
    'city': 'liberio'
}

person_2 = {
    'first': 'zeke',
    'last': 'yeager',
    'age': 29,
    'city': 'liberio'
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"Full Name: {person['first'].title()} {person['last'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")