# pylint: skip-file
import unittest
import os
from unittest.mock import patch
from services.print import Printservice
from services.converter import Converter
from services.console_io import ConsoleIO


class TestPrintservice(unittest.TestCase):
    def setUp(self):
        self.json_file_path = "src/assets/test.json"
        self.converter = Converter(self.json_file_path, ConsoleIO())
        self.json_data = self.converter.return_data()
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
            },
            {
                "type": "book",
                "key": "Albert1946",
                "fields": {
                    "author": "Albert Albretsson",
                    "title": "Albertisms",
                    "publisher": "A.Albertsson",
                    "year": "1946"
                }
            }
        ]
        self.io = ConsoleIO()
        self.printter = Printservice(self.converter, self.io)

    def tearDown(self):
        # Cleanup code: Delete the test.json file
        if os.path.exists(self.json_file_path):
            os.remove(self.json_file_path)
        if os.path.exists("references.bib"):
            os.remove("references.bib")

    def test_regular_print(self):
        self.printter.list_references(False, False)

        self.assertEqual(13, len(self.io.outputs))

    def test_alphabetical_print(self):
        self.printter.list_references(True, False)

        self.assertEqual(13, len(self.io.outputs))

    def test_compact_print(self):
        self.printter.list_references(False, True)

        self.assertEqual(7, len(self.io.outputs))

    def test_compact_alphabetical_print(self):
        self.printter.list_references(True, True)

        if "Albert1946          book          1946 Albert Albretsson   Albertisms" != self.io.outputs[3]:
            self.fail()

        self.assertEqual(7, len(self.io.outputs))

    @patch('builtins.input', return_value='John')
    def test_search(self, mock_input):
        test_value = self.printter.search(False)
        self.assertIn("John", self.io.outputs[0])

    @patch('builtins.input', return_value='John')
    def test_search_by_existing_key(self, mock_input):
        test_value = self.printter.search_by_key(False)
        self.assertIn("John", self.io.outputs[0])

    @patch('builtins.input', return_value='a_nonexistent_key')
    def test_search_by_nonexistent_key(self, mock_input):
        test_value = self.printter.search_by_key(False)
        self.assertEqual(test_value, 0)
