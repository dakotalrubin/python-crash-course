cities = {
    'san diego': {
        'country': 'the united states',
        'population': '3,345,000',
        'fact': 'San Diego shares a southern border with Tijuana, Mexico.'
    },
    'seoul': {
        'country': 'south korea',
        'population': '10,005,000',
        'fact': 'There is a karaoke bar for every 333 people in the city.'
    },
    'paris': {
        'country': 'france',
        'population': '11,277,000',
        'fact': 'The French army still uses carrier pigeons in its ranks.'
    }
}

for city, info in cities.items():
    print(f"{city.title()}")

    for key, value in info.items():
        if key == 'fact':
            print(f"\t{key.title()}: {value}")
        else:
            print(f"\t{key.title()}: {value.title()}")