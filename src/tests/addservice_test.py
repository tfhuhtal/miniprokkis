# pylint: skip-file
import unittest
from unittest.mock import Mock
from services.add import AddService
from services.console_io import ConsoleIO

class TestAddService(unittest.TestCase):
    def setUp(self):
        self.converter = Mock()
        self.converter.return_data.return_value = []
        self.io = ConsoleIO()
        self.add_service = AddService(self.converter, self.io)

    def test_add_reference(self):
        reference = Mock()
        reference.to_json.return_value = {'key': 'testKey', 'type': 'book', 'fields': {}}
        self.add_service.add_reference(reference)
        self.assertEqual(len(self.converter.return_data()), 1)
        self.assertEqual(self.converter.return_data()[0]['key'], 'testKey')

    def test_input_ref_key_valid(self):
        self.io.inputs = ["validKey"]
        result = self.add_service.input_ref_key(["existingKey"])
        self.assertEqual(result, "validKey")

    def test_input_ref_key_invalid(self):
        self.io.inputs = ["invalidKey!!__", "Q"]
        self.add_service.input_ref_key(["existingKey"])
        self.assertIn(
            "\nAvain saa sisältää vain kirjaimia a-z ja numeroita.",
                self.io.outputs)

    def test_input_ref_key_duplicate(self):
        self.io.inputs = ["existingKey", "validKey"]
        result = self.add_service.input_ref_key(["existingKey"])
        self.assertEqual(result, "validKey")

    def test_input_ref_key_cancel(self):
        self.io.inputs = ["Q"]
        result = self.add_service.input_ref_key(["existingKey"])
        self.assertEqual(result, 0)

    def test_input_ref_type(self):
        self.io.inputs = ["1"]
        types = ["book", "article"]
        result = self.add_service.input_ref_type(types)
        self.assertEqual(result, "book")

    def test_input_ref_type_invalid(self):
        self.io.inputs = ["10", "Q"]
        types = ["book", "article"]
        self.add_service.input_ref_type(types)
        self.assertIn("\nVirhe: valitse lähdetyyppi numerolla 1-2", self.io.outputs)

    def test_input_ref_type_cancel(self):
        self.io.inputs = ["Q"]
        types = ["book", "article"]
        result = self.add_service.input_ref_type(types)
        self.assertEqual(result, 0)

    def test_input_ref_fields_cancel(self):
        data = {}
        fields = {"Pakolliset": ["author"]}
        self.io.inputs = ["exit"]
        result = self.add_service.input_ref_fields(data, fields, "Pakolliset")
        self.assertEqual(result, 0)

    def test_input_ref_fields_valid_pakolliset(self):
        data = {}
        data["fields"] = {}
        fields = {"Pakolliset": ["author", "title", "year"], 
                "Vapaaehtoiset": ["volume", "note"]}
        self.io.inputs = ["Martin", "book", "2000"]
        result = self.add_service.input_ref_fields(data, fields, "Pakolliset")
        self.assertEqual(result, 1)
        self.assertEqual(data, {'fields': {'author': 'Martin', 'title': 'book', 'year': '2000'}})

    def test_input_ref_fields_empty_pakolliset(self):
        data = {}
        data["fields"] = {}
        fields = {"Pakolliset": ["author", "title", "year"], 
                "Vapaaehtoiset": ["volume", "note"]}
        self.io.inputs = ["Martin", "book", "", "exit"]
        self.add_service.input_ref_fields(data, fields, "Pakolliset")
        self.assertIn("\nKenttä ei voi olla tyhjä", self.io.outputs)

    def test_input_ref_fields_empty_vapaaehtoiset(self):
        data = {}
        data["fields"] = {}
        fields = {"Vapaaehtoiset": ["volume", "note"]}
        self.io.inputs = ["", ""]
        result = self.add_service.input_ref_fields(data, fields, "Vapaaehtoiset")
        self.assertEqual(data, {'fields': {}})

    def test_input_ref_fields_invalid(self):
        data = {}
        data["fields"] = {}
        fields = {"Pakolliset": ["author", "title", "year"], 
                "Vapaaehtoiset": ["volume", "note"]}
        self.io.inputs = ["Martin", "book", "2000a", "exit"]
        self.add_service.input_ref_fields(data, fields, "Pakolliset")
        self.assertIn("Virhe: (year-kentän tulee olla 4 numeroinen)", self.io.outputs)

    def test_validate_input_year_valid(self):
        result = self.add_service.validate_input("2020", "year")
        self.assertEqual(result, 1)

    def test_validate_input_year_invalid(self):
        result = self.add_service.validate_input("20a0", "year")
        self.assertNotEqual(result, 1)

    def test_validate_input_pages_valid(self):
        result = self.add_service.validate_input("1--10", "pages")
        self.assertEqual(result, 1)

    def test_validate_input_pages_invalid(self):
        result = self.add_service.validate_input("1-10", "pages")
        self.assertNotEqual(result, 1)

    def test_add_with_valid_input(self):
        self.io.inputs = [
            "newValidKey", "1", "Martin", "book", "journal", "2000", "", "", "1--5", "", "", ""]
        self.add_service.add()
        self.assertIn("\nLähde lisätty.", self.io.outputs)
