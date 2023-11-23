"""
Name:Haotian Liu
Date Started:13/11/2023
Brief Project Description:SongListApp is a Kivy-based Python application for managing and tracking a personal song library, offering features to add, sort, and monitor learning status of songs interactively.
GitHub URL:https://github.com/Haot1anLiu/start_a2_songs
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from song import Song
from songcollection import SongCollection

class SongListApp(App):
    def build(self):
        self.collection = SongCollection()
        self.collection.load_songs('songs.json')

        main_layout = BoxLayout(orientation='horizontal')

        # Left side layout
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.5, 1))

        # Sorting spinner
        sort_spinner = Spinner(text='Sort by:', values=('Year', 'Title', 'Learned'))
        sort_spinner.bind(text=self.on_sort_spinner_select)
        left_layout.add_widget(sort_spinner)

        # Text inputs for adding songs
        self.title_input = TextInput(hint_text='Title')
        self.artist_input = TextInput(hint_text='Artist')
        self.year_input = TextInput(hint_text='Year')
        left_layout.add_widget(self.title_input)
        left_layout.add_widget(self.artist_input)
        left_layout.add_widget(self.year_input)

        # Add and Clear buttons
        add_button = Button(text='Add Song')
        add_button.bind(on_press=self.add_song)
        clear_button = Button(text='Clear')
        clear_button.bind(on_press=self.clear_fields)
        left_layout.add_widget(add_button)
        left_layout.add_widget(clear_button)

        # Right side layout (song list and counts)
        right_layout = BoxLayout(orientation='vertical', size_hint=(0.5, 1))
        self.song_count_label = Label(text='Learned: 0, Unlearned: 0')
        right_layout.add_widget(self.song_count_label)
        self.right_layout = right_layout
        main_layout.add_widget(left_layout)
        main_layout.add_widget(right_layout)

        self.update_song_list()
        self.update_song_count()

        return main_layout

    def add_song(self, instance):
        title = self.title_input.text
        artist = self.artist_input.text
        year = int(self.year_input.text) if self.year_input.text.isdigit() else 0
        new_song = Song(title, artist, year)
        self.collection.add_song(new_song)
        self.update_song_list()
        self.update_song_count()

    def clear_fields(self, instance):
        self.title_input.text = ''
        self.artist_input.text = ''
        self.year_input.text = ''

    def update_song_list(self):
        self.right_layout.clear_widgets()
        self.right_layout.add_widget(self.song_count_label)
        for song in self.collection.songs:
            button = Button(text=str(song))
            button.bind(on_press=self.mark_song_learned)
            self.right_layout.add_widget(button)

    def mark_song_learned(self, instance):
        song_title = instance.text.split(' by ')[0]
        for song in self.collection.songs:
            if song.title == song_title:
                song.mark_learned()
                instance.background_color = [0.678, 0.847, 0.902, 1]
                self.update_song_count()
                break

    def update_song_count(self):
        learned = sum(song.is_learned for song in self.collection.songs)
        unlearned = len(self.collection.songs) - learned
        self.song_count_label.text = f"Learned: {learned}, Unlearned: {unlearned}"

    def on_sort_spinner_select(self, spinner, text):
        if text == 'Year':
            self.collection.songs.sort(key=lambda song: song.year)
        elif text == 'Title':
            self.collection.songs.sort(key=lambda song: song.title)
        elif text == 'Learned':
            self.collection.songs.sort(key=lambda song: song.is_learned, reverse=True)
        self.update_song_list()

if __name__ == '__main__':
    SongListApp().run()
