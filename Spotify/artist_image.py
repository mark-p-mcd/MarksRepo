import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from keys import*
import sys
import webbrowser

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_ID,
                                                           client_secret=client_secret))

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Bob Dylan'

results = sp.search(q='artist:' + name, type='artist')

items = results['artists']['items']

if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
webbrowser.open(artist['images'][0]['url'])