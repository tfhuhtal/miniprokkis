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
                    "author": "Albert",
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
        test_value = self.printter.list_references(False, False)

        self.assertEqual(13, len(self.io.outputs))

    def test_alphabetical_print(self):
        test_value = self.printter.list_references(True, False)

        self.assertEqual(13, len(self.io.outputs))

    def test_compact_print(self):
        test_value = self.printter.list_references(False, True)

        self.assertEqual(8, len(self.io.outputs))

    def test_compact_alphabetical_print(self):
        test_value = self.printter.list_references(True, True)

        self.assertEqual(8, len(self.io.outputs))

    @patch('builtins.input', return_value='John')
    def test_search(self, mock_input):
        test_value = self.printter.search(False)
        self.assertIn("John", self.io.outputs[0])
