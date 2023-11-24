"""Tests for Song class."""

from song import Song

def run_tests():
    """
    Run tests to verify the functionality of the Song class.
    """

    # Test creating a Song with default values
    print("Test empty song:")
    default_song = Song()
    print(default_song)  # Display the default song
    # Assertions to ensure the song has default values
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    # Test creating a Song with specified values
    print("\nTest initial-value song:")
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)  # Display the song with specified values
    # Assertions to check if the song has the correct values
    assert initial_song.artist == "Powderfinger"
    assert initial_song.title == "My Happiness"
    assert initial_song.year == 1996
    assert initial_song.is_learned

    # Test toggling the learned status of a song
    print("\nTest toggle_learned_status method:")
    test_song = Song("Unlearned Song", "Unknown Artist", 2000)
    print(f"Initial status: {test_song}")  # Display initial status
    assert not test_song.is_learned  # Check if the song is initially unlearned

    test_song.toggle_learned_status()  # Toggle the learned status
    print(f"Status after learning: {test_song}")  # Display after toggling
    assert test_song.is_learned  # Check if the song is learned

    test_song.toggle_learned_status()  # Toggle the learned status again
    print(f"Status after unlearning: {test_song}")  # Display after toggling again
    assert not test_song.is_learned  # Check if the song is unlearned again

run_tests()