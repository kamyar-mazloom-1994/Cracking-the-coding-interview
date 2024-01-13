import unittest

import PalindromPermutation


class MyTestCase(unittest.TestCase):
    def test_function(self):
        self.assertEqual(PalindromPermutation.pp_checker("tact coa"), True)
        self.assertEqual(PalindromPermutation.pp_checker("young money"), False)


if __name__ == "__main__":
    unittest.main()
