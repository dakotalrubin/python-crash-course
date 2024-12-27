rivers = {
    'nile': 'egypt',
    'colorado': 'the united states',
    'yangtze': 'china',
    'amazon': 'brazil',
    'orinoco': 'venezuela'
}

for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

print("\nThe rivers included in the dictionary are:")

for river in rivers.keys():
    print(f"\t{river.title()}")

print("\nThe countries included in the dictionary are:")

for country in set(rivers.values()):
    print(f"\t{country.title()}")