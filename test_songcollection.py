"""Tests for SongCollection class."""

from song import Song
from songcollection import SongCollection

def run_tests():
    """
    Run tests to verify the functionality of the SongCollection class.
    """

    # Test 1: Creating an empty SongCollection and verifying it's empty
    print("Test empty SongCollection:")
    song_collection = SongCollection()  # Initialize an empty song collection
    print(song_collection)  # Display the empty collection
    assert not song_collection.songs  # Assert that the songs list is empty

    # Test 2: Loading songs from a JSON file and verifying the collection is not empty
    print("Test loading songs:")
    song_collection.load_songs('songs.json')  # Load songs from the specified file
    print(song_collection)  # Display the collection after loading songs
    assert song_collection.songs  # Assert that the collection is not empty after loading

    # Test 3: Adding a new song to the collection and verifying it is added
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))  # Add a new song
    print(song_collection)  # Display the collection after adding the song

    # Test 4, 5, 6: Sorting the songs in the collection based on different attributes
    # and verifying the sort functionality
    for sort_key in ["year", "artist", "title"]:
        print(f"Test sorting - {sort_key}:")
        song_collection.sort(sort_key)  # Sort the collection based on the specified attribute
        print(song_collection)  # Display the sorted collection

    # Test 7: Saving the current state of the song collection to a file
    print("Test saving songs:")
    song_collection.save_songs('songs.json')  # Save the current state of the collection to a file

run_tests()
