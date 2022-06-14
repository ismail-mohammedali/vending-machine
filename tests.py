import unittest
from vending_machine import vendingMachine

class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None: #setting Up Vending machine class 
        self.VM = vendingMachine()
    def test_example1(self): # Test number 1 where 4 quarter are added and Item B is returned
        for i in range(4):
            
            self.assertEqual(self.VM.insertMoney('quarter'),True, "The amount was not added")
        self.assertEqual(self.VM.getItem('itemB'),True, "The Purchase Didn't go through")
    def test_example2(self):# Test number 2 where 2 quarter are added and 2 quarter are returned 
        for i in range(2):
            
            self.assertEqual(self.VM.insertMoney('quarter'),True, "The amount was not added")
        self.assertEqual(self.VM.coinReturn(),{'quarter':2},"Coorect amount was not returned")

    def test_example3(self):# Test number 3 adds a dollar get item and return 35 cents in 25 cents and 10 cents 
        
        self.assertEqual(self.VM.insertMoney('dollar'),True, "The amount was not added")
        self.assertEqual(self.VM.getItem('itemA'),True, "The Purchase Didn't go through")
        self.assertEqual(self.VM.coinReturn(),{'quarter':1,'dime':1},"Coorect amount was not returned")
        
        

if __name__ == '__main__':
    unittest.main()