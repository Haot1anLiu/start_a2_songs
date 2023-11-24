"""
Name: Haotian Liu
Date started: 25/10/2023
GitHub URL: https://github.com/Haot1anLiu/starter_a1_songs
"""

import json

class Song:
    def __init__(self, title, artist, year, learned=False):
        self.title = title  # Song title
        self.artist = artist  # Artist name
        self.year = year  # Release year
        self.learned = learned  # Whether the song has been learned

    def mark_learned(self):
        self.learned = True  # Mark the song as learned

    def __str__(self):
        learned_marker = '*' if not self.learned else ''  # Add a '*' if the song is not learned
        return f"{learned_marker}{self.title} by {self.artist} ({self.year})"  # Format the string to represent song information

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "year": self.year,
            "learned": self.learned
        }

class SongCollection:
    def __init__(self):
        self.songs = []  # Collection of songs

    def add_song(self, song):
        self.songs.append(song)  # Add a song to the collection

    def get_unlearned_songs(self):
        return [song for song in self.songs if not song.learned]  # Get a list of unlearned songs

    def find_song_by_title(self, title):
        for song in self.songs:
            if song.title == title:
                return song  # Find a song by its title
        return None


def display_menu():
    print('Menu:')
    print('D - Display songs')  # Display songs
    print('A - Add new song')  # Add a new song
    print('C - Complete a song')  # Mark a song as learned
    print('Q - Quit')  # Quit the program

def load_songs(filename):
    collection = SongCollection()
    with open(filename, 'r') as file:
        data = json.load(file)
        for song_data in data:
            song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['learned'])
            collection.add_song(song)  # Load song data from the file into the collection
    return collection

def display_data(collection):
    for song in collection.songs:
        print(song)  # Display information about songs in the collection

def add_song_to_collection(collection):
    title = input('Title: ')
    artist = input('Artist: ')
    year = int(input('Year: '))  # Ensure that the input year is an integer
    collection.add_song(Song(title, artist, year))  # Add a new song to the collection
    print(f'{title} by {artist} ({year}) added to Album Tracker')  # Display a message indicating the added song

def mark_song_as_learned(collection):
    title = input("Song title to mark as learned: ")
    for song in collection.songs:
        if song.title == title:
            song.mark_learned()
            print(f'You learned {title}')  # Mark the song as learned and display a message
            break

def save_songs(collection, filename):
    songs_data = [song.to_dict() for song in collection.songs]  # Convert the song collection to a list of dictionaries
    with open(filename, 'w') as file:
        json.dump(songs_data, file)  # Save the song data to a file

def main():
    print("Album Tracker 1.0 - by Haotian Liu")
    collection = load_songs('songs.json')  # Load song data from a file
    print(f'{len(collection.songs)} songs loaded')

    while True:
        display_menu()
        choice = input('>>> ').lower()

        if choice == 'd':
            display_data(collection)  # Display song information
        elif choice == 'a':
            add_song_to_collection(collection)  # Add a new song
        elif choice == 'c':
            mark_song_as_learned(collection)  # Mark a song as learned
        elif choice == 'q':
            save_songs(collection, 'songs.json')  # Save song data to a file
            print(f'{len(collection.songs)} songs saved to songs.json')
            break

if __name__ == '__main__':
    main()