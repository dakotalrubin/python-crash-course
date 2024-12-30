responses = {}

# Create a flag to show that polling is active
active = True

while active:
    # Prompt for the user's name and response
    name = input("\nPlease enter your name: ")
    response = input("Enter the name of a mountain you'd like to climb: ")

    # Store the response in the dictionary
    responses[name] = response

    # Ask if anyone else wants to take the poll
    repeat = input("Would you like to let someone else respond? (yes/no) ")

    if repeat == 'no':
        active = False

# Polling is finished, so show results
print("\nPoll Results:")

for name, response in responses.items():
    print(f"\t{name.title()} would like to climb {response.title()}.")