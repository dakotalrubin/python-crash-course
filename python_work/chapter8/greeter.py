def get_formatted_name(first, last):
    """Return a neatly-formatted full name."""
    full = f"{first} {last}"

    return full.title()

while True:
    print("\nPlease enter your first and last name when prompted.")
    print("(Enter 'quit' to end the program.)")

    first = input("Please enter your first name: ")

    if first == 'quit':
        break

    last = input("Please enter your last name: ")

    if last == 'quit':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nHello, {formatted_name}!")