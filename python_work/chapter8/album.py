def make_album(artist, title, songs=None):
    """Return a dictionary of information about a music album."""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }

    if songs:
        album['songs'] = songs

    return album

album1 = make_album('pink floyd', 'the dark side of the moon')
album2 = make_album('casiopea', 'super flight')
album3 = make_album('stereolab', 'dots and loops')

print(album1)
print(album2)
print(album3)

album4 = make_album('the beach boys', 'pet sounds', 13)

print(album4)