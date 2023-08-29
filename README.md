# glblcd_MP3
Global Code 2023 : MP3 Challenge Example Solution

## Challenge

The aim of this challenge is to implement a Class in Python to maintain an MP3 Playlist. This class could be used when developing the software for a music App on a smartphone or an mp3 player.

This MP3 playlist will be stored as a queue of MP3 tracks. When new tracks are being added to the playlist, they are enqueued at the end of the playlist.

The key features that we will implement within this class are the ability to:

- Load a playlist from a text file
- Display all the tracks from the playlist
- Enqueue (Add) an MP3 to the playlist
- Remove an MP3 from the playlist
- Save a playlist on a text file
- Shuffle all the songs in the playlist
- Count the number of tracks in the playlist
- Calculate the total duration of the playlist
- Clear/Reset the playlist
- Check if the playlist is empty


## Example Solution

This solution is a simple implementation of a possible solution.

There are two example text files containing lists of tracks in this repository:
1. `pop_music.csv` - Pop Music
2. `afro_music.csv` - Afrobeats Music

The Playlist class can be used in the following way with the `pop_music.csv` text file:

### Creating the Playlist and loading tracks

```console
>>> from mp3.playlist import Playlist
>>> pop = Playlist(name="pop")
>>> pop.view()
Playlist: pop
No tracks
0 tracks, 00 hours, 00 minutes, 00 seconds
>>> pop.view()
Playlist: pop
(1): I Gotta Feeling - The Black Eyed Peas [4:52]
(2): Hey Brother - Avicii [4:24]
(3): This is the life - Amy MacDonald [3:08]
(4): World, Hold On - Bob Sinclar [3:39]
(5): Paradise - Coldplay [4:21]
(6): Memories - David Guetta [3:29]
(7): Hot 'n Cold - Katy Perry [4:44]
(8): Our House - Madness [3:47]
(9): Timber - Pitbull [3:35]
9 tracks, 00 hours, 35 minutes, 59 seconds
```

### Adding a track to the playlist
```console
>>> pop.add_track(title="Baby", artist="Justin Bieber", duration="3:34")
>>> pop.view()
Playlist: pop
(1): I Gotta Feeling - The Black Eyed Peas [4:52]
(2): Hey Brother - Avicii [4:24]
(3): This is the life - Amy MacDonald [3:08]
(4): World, Hold On - Bob Sinclar [3:39]
(5): Paradise - Coldplay [4:21]
(6): Memories - David Guetta [3:29]
(7): Hot 'n Cold - Katy Perry [4:44]
(8): Our House - Madness [3:47]
(9): Timber - Pitbull [3:35]
(10): Baby - Justin Bieber [3:34]
10 tracks, 00 hours, 39 minutes, 33 seconds
```

### Shuffling the tracks in the playlist
```console
>>> pop.shuffle()
>>> pop.view()
Playlist: pop
(1): World, Hold On - Bob Sinclar [3:39]
(2): This is the life - Amy MacDonald [3:08]
(3): Our House - Madness [3:47]
(4): Hey Brother - Avicii [4:24]
(5): I Gotta Feeling - The Black Eyed Peas [4:52]
(6): Timber - Pitbull [3:35]
(7): Memories - David Guetta [3:29]
(8): Hot 'n Cold - Katy Perry [4:44]
(9): Baby - Justin Bieber [3:34]
(10): Paradise - Coldplay [4:21]
10 tracks, 00 hours, 39 minutes, 33 seconds
```

### Removing a track from the playlist
```console
>>> pop.remove_track(title="Baby", artist="Justin Bieber")
>>> pop.view()
Playlist: pop
(1): World, Hold On - Bob Sinclar [3:39]
(2): This is the life - Amy MacDonald [3:08]
(3): Our House - Madness [3:47]
(4): Hey Brother - Avicii [4:24]
(5): I Gotta Feeling - The Black Eyed Peas [4:52]
(6): Timber - Pitbull [3:35]
(7): Memories - David Guetta [3:29]
(8): Hot 'n Cold - Katy Perry [4:44]
(9): Paradise - Coldplay [4:21]
9 tracks, 00 hours, 35 minutes, 59 seconds
```

### Resetting/Clearing the Playlist
```console
>>> pop.clear()
>>> pop.view()
Playlist: pop
No tracks
0 tracks, 00 hours, 00 minutes, 00 seconds
```