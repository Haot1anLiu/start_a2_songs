# Import the JSON module for file operations and the Song class
import json
from song import Song

# Define the SongCollection class
class SongCollection:
    # Constructor for creating a new song collection
    def __init__(self):
        self.songs = []  # Initialize an empty list to store songs

    # Method to add a new song to the collection
    def add_song(self, song):
        self.songs.append(song)  # Add the provided song to the collection

    # Method to load songs from a JSON file
    def load_songs(self, filename):
        try:
            with open(filename, 'r') as file:  # Open the file for reading
                data = json.load(file)  # Load the JSON data from the file
                for song_data in data:  # Iterate over each song in the data
                    self.songs.append(Song(**song_data))  # Create a Song object and add it to the collection
        except FileNotFoundError:
            pass  # If the file is not found, do nothing (ignore the error)

    # Method to save the current collection of songs to a JSON file
    def save_songs(self, filename):
        with open(filename, 'w') as file:  # Open the file for writing
            # Convert each song to a dictionary and save as JSON
            json.dump([song.__dict__ for song in self.songs], file)

    # Method to get a list of learned songs
    def get_learned_songs(self):
        # Return a list of songs where the is_learned attribute is True
        return [song for song in self.songs if song.is_learned]

    # Method to get a list of unlearned songs
    def get_unlearned_songs(self):
        # Return a list of songs where the is_learned attribute is False
        return [song for song in self.songs if not song.is_learned]
