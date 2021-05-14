import unittest 

from classes.room import Room 
from classes.song import Song 
from classes.bar import Bar 
from classes.guest import Guest 

class TestRoom(unittest.TestCase):
    
    def setup(self):
        self.room = Room("codeclan_caraoke_room_1", 8 , [], [])
        
        self.guest1 = Guest("Sarah",50, "This Charming Man", "The Smiths")
        self.guest2 = Guest("Verbena", 100, "Disturbed ","sound of silence")
        self.guest3 = Guest("Keith Douglas", 0, "The Beach Boys"," I get Around")
        self.song1 = Song("The Passanger", "Iggy Pop")
        self.song2  = Song("Runaway Train", "Soul Asylum")
        self.song3 = Song("Demons","Imagine Dragons")
        self.bar = Bar("The Mighty Session", [self.room], 25, 0 ["Gin And Tonic","Espresso martini","Wine"])
        
    def test_room_name(self):
        self.assertAlmostEqual("codeclan_caraoke_room_1", self.room.name) 
        
    def test_max_capacity(self):
        self.assertEqual(8, self.room.max_capacity)
        
    def test_room_starts_empty(self):
        self.assertEqual(0, len(self.room.guests))
        
    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest1)
        self.assertEqual(1, len(self.room.guests))
    
    def test_add_guest_to_room_max_capacity(self):
        self.room.guest = [self.guest1, self.guest2, self.guest3,self.guest1, self.guest2, self.guest3,self.guest1, self.guest2]
        self.room.add_guest_to_room(self.guest3)
        self.assertEqual(8, len(self.room.guests))
    
    def test_remove_guest_from_room(self):
        self.room.guests = [self.guest1, self.guest2]
        self.room.remove_guest_from_room(self.guest1, self.bar)
        self.assertEqual(1, len(self.room.guests))
        
    def add_new_song_to_playlist(self):
        self.room.add_new_song_to_playlist(self.song1)
        self.assertEqual(self.song1, self.room.playlist[0])
        
    def test_length_of_playlist(self):
        self.room.playlist = [self.song1,self.song2]
        self.assertEqual(2,len(self.room.playlist))
        
    def test_remove_song_from_playlist(self):
        self.room.playlist = [self.song1, self.guest2]
        self.room.remove_song_from_playlist(self.song2)
        self.assertEqual(1, len(self.room.playlist))
        
    def test_check_favourite_song_present(self):
        self.room.guests = [self.guest1, self.guest2]
        self.room.playlist = [self.song1, self.song2]
        self.assertEqual("Oh I love this one!",self.room.check_favourite_song(self.guest2))
    
    def test_check_favourite_song_not_present(self):
        self.room.guests = [self.guest1, self.guest2]
        self.room.playlist = [self.song1, self.song2] 
        self.assertEqual("No why isn't my favourite here",self.room.check_favourite_song(self.guest2))
        