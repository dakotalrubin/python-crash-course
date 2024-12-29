favorite_places = {
    'dakota': ['coronado', 'monterey', 'laguna beach'],
    'dylan': ['san diego', 'boston', 'hoboken'],
    'jared': ['sacramento', 'santa cruz', 'seattle']
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")

    for place in places:
        print(f"\t{place.title()}")