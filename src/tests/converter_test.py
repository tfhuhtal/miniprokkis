# pylint: skip-file
import unittest
import os
from services.converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.json_file_path = "src/assets/test.json"
        self.converter = Converter(self.json_file_path)
        self.converter.json_data = [
            {
                "type": "book",
                "key": "John2020",
                "fields": {
                    "author": "Johnson",
                    "title": "Johnsonisms",
                    "publisher": "J.Johnson",
                    "year": "2020"
                }
            }
        ]

    def tearDown(self):
        # Cleanup code: Delete the test.json file
        if os.path.exists(self.json_file_path):
            os.remove(self.json_file_path)
        if os.path.exists("references.bib"):
            os.remove("references.bib")

    def test_save_json(self):
        self.converter.save_json()
        self.assertTrue(os.path.isfile(self.json_file_path))

    def test_convert(self):
        self.assertEqual(
            self.converter.convert(),
            '[{"type": "book", "key": "John2020", "fields": {"author": "Johnson", "title": "Johnsonisms", "publisher": "J.Johnson", "year": "2020"}}]')

    def test_convert_json_to_bibtex(self):
        self.assertEqual(
            self.converter.convert_json_to_bibtex(),
            '@book{John2020,\n  author = {Johnson},\n  title = {Johnsonisms},\n  publisher = {J.Johnson},\n  year = {2020}\n}\n')

    def test_return_data(self):
        self.assertEqual(self.converter.return_data(),
                         [{'type': 'book',
                           'key': 'John2020',
                           'fields': {'author': 'Johnson',
                                      'title': 'Johnsonisms',
                                      'publisher': 'J.Johnson',
                                      'year': '2020'}}])

    def test_load_json(self):
        self.converter._load_json()
        self.assertTrue(os.path.isfile(self.json_file_path))

    def test_bibtex_to_file(self):
        self.converter.bibtex_to_file()
        self.assertTrue(os.path.isfile("references.bib"))
