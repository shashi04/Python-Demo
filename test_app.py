import unittest
from app import hello

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Welcome to Jenkins Class 1!")

if __name__ == "__main__":
    unittest.main()
