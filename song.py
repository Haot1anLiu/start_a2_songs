"""Song Class"""

# Define the Song class
class Song:
    # Constructor for creating a new song instance
    def __init__(self, title, artist, year, is_learned=False):
        # Initialize the song with title, artist, year, and learning status
        self.title = title  # Title of the song
        self.artist = artist  # Artist or band name
        self.year = year  # Release year of the song
        self.is_learned = is_learned  # Boolean flag to track if the song is learned

    # String representation of a Song object
    def __str__(self):
        # Format the song information as a string
        # If the song is not learned, a '*' is added to the string
        return f"{self.title} by {self.artist} ({self.year}) {'*' if not self.is_learned else ''}"

    # Method to mark the song as learned
    def mark_learned(self):
        # Set the is_learned flag to True indicating the song is learned
        self.is_learned = True

    # Method to mark the song as unlearned
    def mark_unlearned(self):
        # Set the is_learned flag to False indicating the song is not learned
        self.is_learned = False
