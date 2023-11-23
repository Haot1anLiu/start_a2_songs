"""Song Class"""

class Song:
    def __init__(self, title, artist, year, is_learned=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.year}) {'*' if not self.is_learned else ''}"

    def mark_learned(self):
        self.is_learned = True

    def mark_unlearned(self):
        self.is_learned = False
