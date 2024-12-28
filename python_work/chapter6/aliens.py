# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change the first 3 green aliens into yellow aliens
# If any of the first 3 aliens are already yellow, change them into red aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print("...")

# Show how many aliens have been created
print(f"\nTotal number of aliens: {len(aliens)}")