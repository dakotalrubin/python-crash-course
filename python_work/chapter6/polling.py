favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi, {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("\nThe following programming languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(f"\t{language.title()}")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!\n")
    
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\n")

polling_names = ['jen', 'edward', 'hoss', 'ben']

for name in polling_names:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take our poll!")