allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])

#Checkpoint 2:
bad_tags = {tag for tag in tag_set if tag not in allowed_tags}

for tags in bad_tags:
  if tags in tag_set:
    tag_set.remove(tags)

song_data_users['Retro Words']= tag_set
print(song_data_users)
