import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter("exampl.json")

    def test_convert(self):
        self.assertEqual(self.converter.convert(), "{}")
