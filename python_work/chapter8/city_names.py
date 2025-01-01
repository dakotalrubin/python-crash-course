def city_country(city, country):
    """Return a neatly-formatted location."""
    location = f"{city.title()}, {country.title()}"
    return location

pair1 = city_country('san diego', 'united states')
pair2 = city_country('rio de janeiro', 'brasil')
pair3 = city_country('vancouver', 'canada')

print(pair1)
print(pair2)
print(pair3)