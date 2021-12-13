import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from keys import*
import pprint as pp
import json
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_ID,
                                                           client_secret=client_secret))
# print top 20 songs froma given artist
name = 'Sting'
resultsArtist = sp.search(q='artist:'+ name, type='artist', limit=20)
resultsTrack = sp.search(q='artist:'+ name, limit=20)

links = resultsTrack['tracks']['items']
print(type(links))
links1 = links[0]

album_images = links1['album']['images']
pp.pprint(album_images[0]['url'])
pp.pprint(links[0]['artists'][0]['name']) #prints the artist name of first element
count = 1
for idx, track in enumerate(resultsTrack['tracks']['items']):
    if resultsTrack['tracks']['items'][idx]['artists'][0]['name'] == name:
        print(count, track['name'], resultsTrack['tracks']['items'][idx]['album']['images'][0]['url'])
        count = count + 1