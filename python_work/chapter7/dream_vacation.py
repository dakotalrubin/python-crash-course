responses = {}

active = True

while active:
    name = input("\nPlease enter your name: ")
    response = input("Please enter your dream vacation destination: ")

    responses[name] = response

    repeat = input("Would someone else like to respond? (yes/no) ")

    if repeat == 'no':
        active = False

print("\nPoll Results:")

for name, response in responses.items():
    print(f"\t{name.title()} would like to visit {response.title()}.")