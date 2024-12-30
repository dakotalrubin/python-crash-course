prompt = "\nEnter a topping you want to add to your pizza:"
prompt += "\n(Enter 'quit' to end the program.) "

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")