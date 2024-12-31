def describe_city(city, country='the united states'):
    """Print a message describing a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('san diego')
describe_city(city='new york city')
describe_city('rio de janeiro', 'brasil')