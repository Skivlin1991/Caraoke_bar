import unittest

from classes.song import Song 

class TestSong(unittest.TestCase):
    
    def setup(self):
        self.song = Song("death to all but metal", "steel panther")
        
    def test_song_name(self):
        self.assertEqual("death to all but metal", self.song.name)
        
    def test_song_artist(self):
        self.assertEqual("steel panther",self.song.artest)