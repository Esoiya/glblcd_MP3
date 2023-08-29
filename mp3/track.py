import re


class Track:
    """Track class"""

    def __init__(self, title: str, artist: str, duration: str) -> None:
        """Track initialisation method

        Args:
            title (str): Track title
            artist (str): Track artist
            duration (str): Track duration
        """
        self.title: str = title
        self.artist: str = artist
        self.length: str = duration

    def __str__(self) -> str:
        return f"{self.title} - {self.artist} [{self.length}]"

    def __eq__(self, other: "Track") -> bool:
        return (self.title == other.title) and (self.artist == other.artist) and (self.length == other.length)
    
    
    def duration(self, seconds: bool = False) -> int:
        """Track duration

        Args:
            seconds (bool, optional): Seconds flag. Defaults to False.

        Returns:
            int: Track duration
        """
            
        
        len_attrs = re.findall("\d+", self.length)
        dur_secs: int = int(len_attrs.pop())
        dur_mins: int = int(len_attrs.pop())
        dur_hours: int = 0
        
        if len(len_attrs) == 1:
            dur_hours = len_attrs.pop()
        
        if seconds:
            return dur_secs + (dur_mins * 60) + ( dur_hours * 3600)
        
        return self.length

            