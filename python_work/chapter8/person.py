def build_person(first, last, age=None):
    """Return a dictionary of information about a person."""
    person = {
        'first': first,
        'last': last
    }

    if age:
        person['age'] = age

    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)