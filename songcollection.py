"""songcollection"""

import json
from song import Song

class SongCollection:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def load_songs(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for song_data in data:
                    self.songs.append(Song(**song_data))
        except FileNotFoundError:
            pass  # Handle file not found

    def save_songs(self, filename):
        with open(filename, 'w') as file:
            json.dump([song.__dict__ for song in self.songs], file)

    def get_learned_songs(self):
        return [song for song in self.songs if song.is_learned]

    def get_unlearned_songs(self):
        return [song for song in self.songs if not song.is_learned]
