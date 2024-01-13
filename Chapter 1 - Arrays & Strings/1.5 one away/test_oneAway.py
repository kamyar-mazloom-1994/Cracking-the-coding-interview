import unittest

import OneAway


class MyTestCase(unittest.TestCase):
    def test_function(self):
        self.assertEqual(OneAway.one_away("pale", "pal"), True)
        self.assertEqual(OneAway.one_away("pale", "bale"), True)
        self.assertEqual(OneAway.one_away("pales", "pale"), True)
        self.assertEqual(OneAway.one_away("pale", "bake"), False)
        self.assertEqual(OneAway.one_away("pale", "ba"), False)


if __name__ == "__main__":
    unittest.main()
