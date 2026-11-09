
import unittest
from app import add, subtract, multiply

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_subtract(self):
        self.assertEqual(subtract(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(multiply(5, 5), 25)

if __name__ == "__main__":
    unittest.main()
