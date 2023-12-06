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

    def test_input_ref_key_duplicate(self):
        self.io.inputs = ["existingKey", "validKey"]
        result = self.add_service.input_ref_key(["existingKey"])
        self.assertEqual(result, "validKey")

    def test_input_ref_key_cancel(self):
        self.io.inputs = [""]
        result = self.add_service.input_ref_key(["existingKey"])
        self.assertEqual(result, 0)

    def test_validate_input_year_valid(self):
        result = self.add_service.validate_input("2020", "year")
        self.assertEqual(result, 1)

    def test_validate_input_year_invalid(self):
        result = self.add_service.validate_input("20a0", "year")
        self.assertNotEqual(result, 1)
