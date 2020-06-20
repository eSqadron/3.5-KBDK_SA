import unittest
from main import ShoppingList

class MyTestCase(unittest.TestCase):
    def test_constructor_name(self):
        sl = ShoppingList("name")
        self.assertEqual(sl.name_, "name")


if __name__ == '__main__':
    unittest.main()
