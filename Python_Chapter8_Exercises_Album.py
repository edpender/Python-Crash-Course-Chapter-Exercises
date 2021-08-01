def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('bruce sprinsteen', 'born to run')
print(album)

album = make_album('the clash', 'london calling')
print(album)

album = make_album('fleetwood mac', 'rumours')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)
