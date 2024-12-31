def build_person(first, last):
    """Return a dictionary of information about a person."""
    person = {
        'first': first,
        'last': last
    }

    return person

musician = build_person('jimi', 'hendrix')
print(musician)