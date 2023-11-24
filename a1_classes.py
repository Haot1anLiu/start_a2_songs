"""
Name: Haotian Liu
Date started: 25/10/2023
GitHub URL: https://github.com/Haot1anLiu/starter_a1_songs
"""

import json

class Song:
    def __init__(self, title, artist, year, learned=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.learned = learned

    def mark_learned(self):
        self.learned = True

    def __str__(self):
        learned_marker = '*' if not self.learned else ''
        return f"{learned_marker}{self.title} by {self.artist} ({self.year})"

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "year": self.year,
            "learned": self.learned
        }

class SongCollection:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_unlearned_songs(self):
        return [song for song in self.songs if not song.learned]

    def find_song_by_title(self, title):
        for song in self.songs:
            if song.title == title:
                return song
        return None


def display_menu():
    print('Menu:')
    print('D - Display songs')
    print('A - Add new song')
    print('C - Complete a song')
    print('Q - Quit')

def load_songs(filename):
    collection = SongCollection()
    with open(filename, 'r') as file:
        data = json.load(file)
        for song_data in data:
            song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['learned'])
            collection.add_song(song)
    return collection

def display_data(collection):
    for song in collection.songs:
        print(song)

def add_song_to_collection(collection):
    title = input('Title: ')
    artist = input('Artist: ')
    year = int(input('Year: '))  # 确保输入年份为整数
    collection.add_song(Song(title, artist, year))
    print(f'{title} by {artist} ({year}) added to Album Tracker')

def mark_song_as_learned(collection):
    title = input("Song title to mark as learned: ")
    for song in collection.songs:
        if song.title == title:
            song.mark_learned()
            print(f'You learned {title}')
            break

def save_songs(collection, filename):
    songs_data = [song.to_dict() for song in collection.songs]  # 假设 Song 类有一个 to_dict 方法
    with open(filename, 'w') as file:
        json.dump(songs_data, file)

def main():
    print("Album Tracker 1.0 - by Haotian Liu")
    collection = load_songs('songs.json')
    print(f'{len(collection.songs)} songs loaded')

    while True:
        display_menu()
        choice = input('>>> ').lower()

        if choice == 'd':
            display_data(collection)
        elif choice == 'a':
            add_song_to_collection(collection)
        elif choice == 'c':
            mark_song_as_learned(collection)
        elif choice == 'q':
            save_songs(collection, 'songs.json')
            print(f'{len(collection.songs)} songs saved to songs.json')
            break

if __name__ == '__main__':
    main()
