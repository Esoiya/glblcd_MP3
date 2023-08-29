import random
import time
from typing import List


from mp3.track import Track


class Playlist:
    """MP3 Playlist Class"""
    
    def __init__(self, name: str, shuffle: bool = False) -> None:
        """Playlist initalisation method

        Args:
            name (str): Playlist name
            shuffle (bool, optional): Shuffle flag. Defaults to False.
        """
        self.name: str = name
        self._shuffle: bool = shuffle
        self.tracks: List[Track] = []
    
    def load(self, filename: str) -> None:
        """Load tracks into playlist from specified file

        Args:
            filename (str): filename of ; separated file \
                containing the list of tracks.
        """
        print(f"Loading tracks from CSV file : {filename}")
        track_file = open(filename, "r")
        for track in track_file:
            metadata = track.split(";")
            if len(metadata) == 4:
                self.tracks.append(
                    Track(
                        title=metadata[0],
                        artist=metadata[1],
                        duration=metadata[2]
                    )
                )
        track_file.close()
        
        if self._shuffle:
            self.shuffle()
        
    def view(self) -> None:
        """Display information about the playlist:\
            - Display name of the playlist
            - List all of the tracks
            - Display the number of tracks and total playtime
        """
        print(f"Playlist: {self.name}")
        
        if self.isEmpty():
            print("No tracks")
            
        else:    
            trackNum: int = 1
            for track in self.tracks:
                print(f"({trackNum}): {track}")
                trackNum += 1
        print(self.metadata())


    def add_track(self, title: str, artist: str, duration: str) -> None:
        """Add a track to the playlist

        Args:
            title (str): Track title
            artist (str): Track Artist
            duration (str): Track duration. Duration must be in the form 1:45 or 1:45:40.
        """
        track: Track = Track(
            title=title,
            artist=artist,
            duration=duration
        )
        self.tracks.append(track)
        
    def remove_track(self, title: str, artist: str) -> None:
        """Remove a track from the playlist

        Args:
            title (str): Title of the track
            artist (str): Artist of the track
        """
        filtered_tracks = list(filter(lambda x: x.title != title and x.artist != artist, self.tracks))
        self.tracks = filtered_tracks
        
    def shuffle(self):
        """Shuffle the playlist tracks
        """
        random.shuffle(self.tracks)
        self._shuffle = True
        
    def clear(self):
        """Clear the playlist tracks
        """
        self.tracks = []
        
    def isEmpty(self) -> bool:
        """Check if Playlist is empty

        Returns:
            bool: True if the playlist is empty, False if not.
        """
        return not self.tracks
    
    def metadata(self) -> str:
        """Display Playlist metadata

        Returns:
            str: Number of tracks in the playlist and the total playtime
        """
        track_durations: List[int] = [track.duration(seconds=True) for track in self.tracks]
        track_count: int = len(self.tracks)
        
        play_time_seconds: float = sum(track_durations)
        
        play_time: str = time.strftime(
            "%H hours, %M minutes, %S seconds", time.gmtime(play_time_seconds)
        )
        
        return f"{track_count} tracks, {play_time}"
    
    def save(self) -> None:
        """Save the current playlist to a csv file with the name of the playlist.
        """
        print(f"Saving Playlist {self.name} to CSV file")
        
        with open(f"{self.name}.csv", "w") as playlist_file:
            for track in self.tracks:
                playlist_file.write(f"{track.title};{track.artist};{track.length};\n")
        
        print(f"Saved playlist to file: {self.name}.csv")
