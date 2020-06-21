import unittest
from main import ShoppingList, ListNameLengthError, ListNameAlreadyTakenError


class test_constructor(unittest.TestCase):
    def test_name_setting(self):
        sl = ShoppingList("name")
        self.assertEqual(sl.name_, "name")

    def test_name_setting_length_short(self):
        sl = ShoppingList("name")

    def test_name_setting_length_long(self):
        self.assertRaises(ListNameLengthError, ShoppingList("namefffffffffffffffffffffffffff"))

    def test_name_not_taken(self):
        listsList = [ShoppingList("name")]
        self.assertRaises(ListNameAlreadyTakenError, ShoppingList("name"))

if __name__ == '__main__':
    unittest.main()
