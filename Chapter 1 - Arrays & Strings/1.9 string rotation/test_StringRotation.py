import unittest

import StringRotation


class MyTestCase(unittest.TestCase):
    def test_function(self):
        self.assertEqual(
            StringRotation.string_rotation("waterbottle", "erbottlewat"), True
        )
        self.assertEqual(
            StringRotation.string_rotation("wrong money", "young money"), False
        )


if __name__ == "__main__":
    unittest.main()
