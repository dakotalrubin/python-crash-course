prompt = "\nEnter your age for movie ticket pricing:"
prompt += "\n(Enter 'quit' to end the program.) "

active = True

while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            message = "Your ticket is free!"
        elif age < 12:
            message = "Your ticket is $10."
        else:
            message = "Your ticket is $15."

        print(message)