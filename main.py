import lyricsgenius
import json

genius = lyricsgenius.Genius("6lC3TdF181uu0sWTqZJmRnU0iPOIzlMoBSSVj8mlVzXbpbth1oiP8IeWmwaJD69s",
                             verbose = False,
                             skip_non_songs = False
                             )

#%%

artist_name= "Okaber"
artist = genius.search_artist(f"{artist_name}", sort="title")

#%%

artist.save_lyrics()

#%%

with open(f"Lyrics_{artist_name}.json", "r") as read_file:
    data = json.load(read_file)


#%%
lyrics = ''
for songs in data['songs']:
    print(songs['full_title'])
    lyrics += '\n'+'\n' + songs['lyrics']

#%%

text_file = open(f'{artist_name}.txt', "wt", encoding='utf-8')
text_file.write(lyrics)
