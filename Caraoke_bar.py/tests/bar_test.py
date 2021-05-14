import unittest

from classes.bar import Bar
from classes.guest import Guest
from classes.song import Song 
from classes.room import Room

class TestBar(unittest.TestCase):
    
    def setup(self):
        self.room = Room("codeclan_caraoke_room_1", 8 ,[], [])
        self.guest1 = Guest("Sarah",20, "This Charming Man", "The Smiths")
        self.guest2 = Guest("Verbena", 30, "Disturbed ","sound of silence")
        self.guest3 = Guest("Keith Douglas", 50, "The Beach Boys"," I get Around")
        
        self.song1 = Song("The Passanger", "Iggy Pop")
        self.song2  = Song("Runaway Train", "Soul Asylum")
        self.song3 = Song("Demons","Imagine Dragons")
        
        self.bar = Bar("The Mighty Session", [self.room], 25, 0 ["Gin And Tonic","Espresso martini","Wine"])
        
    def test_bar_name(self):
        self.assertEqual("The Mighty Session", self.bar.name)
        
    def test_bar_rooms(self):
        self.assertEqual(1, len(self.bar.karaoke_rooms))
        
    def test_bar_entry_price(self):
        self.assertEqual(20, self.bar.entry_price)
        
    def test_bar_looby_empty(self):
        self.assertEqual(0,len(self.bar.bar_lobby))
        
    def test_bar_total_guests(self):
        self.assertEqual(0,len(self.bar.bar_lobby))
    
    def test_add_guest_to_looby_looby_size(self):
        self.bar.add_guest_to_bar_lobby(self.guest1)
        self.assertEqual(1,len(self.bar.bar_lobby))
        
    def test_add_guest_to_bar_lobby_till(self):
        self.bar.add_guest_to_bar_lobby(self.guest1)
        self.assertEqual(20, self.bar.till)
        
    def test_add_guest_to_bar_not_enough_money_looby_size(self):
        self.bar.add_guest_to_bar_lobby(self.guest3)
        self.assertEqual(0,len(self.bar.bar_lobby))
        
    def test_add_guest_to_bar_not_enough_money_till(self):
        self.bar.add_guest_to_bar_lobby(self.guest3)
        self.assertEqual(0, len(self.bar.karaoke_room))
        
    def test_create_new_karaoke_room(self):
        self.bar.create_new_karaoke_room("codeclan_coraoke_room_2")
        self.assertEqual(2, len(self.bar.karaoke_rooms))
        
    def test_remove_karaoke_room(self):
        self.bar.karaoke_rooms = ["codeclan_caraoke_room_1","codeclan_caraoke_room_2"]
        self.bar.remove_karaoke_room("codeclan_caraoke_room_1")
        self.assertEqual(1, len(self.test_bar_karaoke_rooms))
        
    def test_send_guest_to_karaoke_room(self):
        self.bar.lobby = [self.guest1, self.guest2, self.guest3]
        self.bar.karaoke_rooms = [self.room]
        self.bar.send_guest_to_karaoke_room(self.guest1,self.room, self.bar)
        self.assertEqual(1, len(self.room.guests))
        
    def test_customer_beer_order_enough_money_response_check(self):
         self.assertEqual("Enjoy", self.bar.customer_beer_order(self.guest1))
         
    def test_customer_beer_order_enough_money_wallet_check(self):
        self.bar.customer_beer_order(self.guest1)
        self.assertEqual(45, self.guest1.wallet)
        
    def test_customer_beer_order_enough_money_till_check(self):
        self.bar.customer_beer_order(self.guest1)
        self.assertEqual(5, self.bar.till)
        
    def test_customer_order_not_enough_money_response_check(self):
        self.assertEqual("no gin for you ,that's sad", self.bar.customer_beer_order(self.guest3))
        
     def test_customer_beer_order_not_enough_money_wallet_check(self):
            self.bar.customer_beer_order(self.guest3)
        self.assertEqual(0, self.guest3.wallet)
        
    def test_customer_beer_order_not_enough_money_till_check(self):
        self.bar.customer_beer_order(self.guest3)
        self.assertEqual(0, self.bar.till)
    
     def test_total_guests_number_empty(self):
            self.assertEqual(0, self.bar.total_guests_number(self.room))
    
    def test_total_guests_number_busy(self):
        self.bar.bar_lobby = [self.guest1, self.guest2]
        self.room.guests = [self.guest3]
        self.assertEqual(3, self.bar.total_guests_number(self.room))

    def test_add_drink_to_drink_list(self):
        self.bar.add_drink_to_drink_list("Corona")
        self.assertEqual(2, len(self.bar.drinks_list))

    def test_remove_drink_from_drink_list(self):
        self.bar.remove_drink_from_drink_list("Guinness")
        self.assertEqual(0, len(self.bar.drinks_list))