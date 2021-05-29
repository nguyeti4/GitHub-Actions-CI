import unittest
import example


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(example.add(1,2),3)


if _name_ == '_main_':
    unittest.main()