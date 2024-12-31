def get_formatted_name(first, last, middle=''):
    """Return a neatly-formatted full name."""
    if middle:
        full = f"{first} {middle} {last}"
    else:
        full = f"{first} {last}"

    return full.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)