import unittest
import checkPermutation


class MyTestCase(unittest.TestCase):
    def test_function(self):
        self.assertEqual(checkPermutation.check_permutation("aba","baa"),True)
        self.assertEqual(checkPermutation.check_permutation("aba", "baaa"), False)
        self.assertEqual(checkPermutation.check_permutation("aba", "bca"), False)
        self.assertEqual(checkPermutation.check_permutation("bac", "ba"), False)


if __name__ == '__main__':
    unittest.main()
