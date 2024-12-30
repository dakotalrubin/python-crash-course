prompt = "\nEnter your age for movie ticket pricing:"
prompt += "\n(Enter 'quit' to end the program.) "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            message = "Your ticket is free!"
        elif age < 12:
            message = "Your ticket is $10."
        else:
            message = "Your ticket is $15."

        print(message)