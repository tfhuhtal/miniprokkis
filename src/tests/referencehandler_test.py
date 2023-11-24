import unittest
from referencehandler import ReferenceHandler
from reference_types import ReferenceTypes


class ConverterStub:
    def __init__(self, json_file_path):
        self.json_data = [{
        "type": "book",
        "key": "John2020",
        "fields": {
            "author": "Johnson",
            "title": "Johnsonisms",
            "publisher": "J.Johnson",
            "year": "2020"
        }
    }]

    def get_keys(self):
        return [entry['key'] for entry in self.json_data]

    def add_reference(self, reference):
        self.json_data.append(reference.to_json())

    def delete_reference(self, reference_key):
        self.json_data = [entry for entry in self.json_data if entry['key'] != reference_key]


class ConsoleIOStub:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)

    def read(self, prompt):
        self.outputs.append(prompt)
        return self.inputs.pop(0) if self.inputs else ''

class TestReferenceHandler(unittest.TestCase):
    def setUp(self):
        self.io_stub = ConsoleIOStub()
        self.converter_stub = ConverterStub('testi')
        self.handler = ReferenceHandler(self.io_stub, self.converter_stub)

    def test_add_reference(self):
        self.io_stub.inputs = ['ref_key', 'book', 'author', 'title', 'publisher', 'year', '', '', '', '', '']
        self.handler.add()
        self.assertEqual(self.io_stub.outputs[-1], "\nLähde lisätty.")

    def test_delete_reference(self):
        self.io_stub.inputs = ['John2020']
        self.handler.delete()
        self.assertEqual(self.io_stub.outputs[-1], "\nLähde poistettu.")
