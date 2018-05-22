import unittest
from boggle import check

class TestBoggle(unittest.TestCase):
    def test_is_this_thing_on(self):
        self.assertEqual(check(),1)