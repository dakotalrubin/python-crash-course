favorite_numbers = {
    'kevin': [32, 16, 43],
    'jack': [24, 138, 99],
    'johnny': [1000, 22, 7],
    'maria': [42, 777, 1],
    'dakota': [238, 29, 99]
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:")

    for number in numbers:
        print(f"\t{number}")