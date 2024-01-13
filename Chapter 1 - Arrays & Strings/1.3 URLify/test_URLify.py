import unittest

import URLify


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(URLify.urlify("young money", 11), "young%20money")


if __name__ == "__main__":
    unittest.main()
