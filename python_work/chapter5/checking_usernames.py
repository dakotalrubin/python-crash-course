current_users = ['adam', 'becky', 'charles', 'johnny', 'trixie']
current_users_lower = current_users[:]

new_users = ['adam', 'jack', 'jason', 'paulie', 'becky']

for username in new_users:
    if username.lower() in current_users_lower:
        print(f"Sorry, '{username}'. You'll have to pick a new username.")
    else:
        print(f"The username '{username}' is available!")