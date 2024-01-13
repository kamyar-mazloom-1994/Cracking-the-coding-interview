import unittest

import StringCompression


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(
            StringCompression.string_compression("aaabbbcccddd"), "a3b3c3d3"
        )
        self.assertEqual(StringCompression.string_compression("aaabbbcccd"), "a3b3c3d1")
        self.assertEqual(StringCompression.string_compression("abcd"), "abcd")


if __name__ == "__main__":
    unittest.main()
