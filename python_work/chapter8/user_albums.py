def make_album(artist, title):
    """Return a dictionary of information about a music album."""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }

    return album

while True:
    print("\nEnter an artist name and album title when prompted.")
    print("(Enter 'quit' to end the program at any time.)")

    artist = input("Enter an artist name: ")

    if artist == 'quit':
        break

    title = input("Enter an album title: ")

    if title == 'quit':
        break

    album = make_album(artist, title)
    print(album)