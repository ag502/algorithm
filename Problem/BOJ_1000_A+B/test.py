import unittest
from main import main


class MyTest(unittest.TestCase):
    def test_main(self):
        result = main()
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()