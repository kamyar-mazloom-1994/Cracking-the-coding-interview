import unittest
import uniqueCheck


class MyTestCase(unittest.TestCase):
    def test_unique_check(self):
        self.assertEqual(uniqueCheck.unique_check("1234567890qwertyuiopasdfghjklzxcvbnm"), True)
        self.assertEqual(uniqueCheck.unique_check("1234567890qwertyuiopasdfghjklzxfcvbnm"), False)

    def test_empty_string(self):
        self.assertEqual(uniqueCheck.unique_check(""), True)

if __name__ == '__main__':
    unittest.main()
