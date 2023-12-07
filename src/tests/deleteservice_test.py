# pylint: skip-file
import unittest
from unittest.mock import Mock
from services.add import AddService
from services.delete import DeleteService
from services.console_io import ConsoleIO

class TestDeleteService(unittest.TestCase):
    def setUp(self):
        self.converter = Mock()
        self.converter.return_data.return_value = []
        self.io = ConsoleIO()
        self.adder = AddService(self.converter, self.io)
        self.deleter = DeleteService(self.converter, self.io)

    def test_delete_reference_validkey(self):
        reference = Mock()
        reference.to_json.return_value = {'key': 'ValidKey', 'type': 'book', 'fields': {}}
        self.adder.add_reference(reference)
        self.io.inputs = ["ValidKey"]
        self.deleter.delete()
        self.assertAlmostEqual(['\nLähde poistettu.'], self.io.outputs)
    
    def test_delete_reference_invalidkey(self):
        self.io.inputs = ["InvalidKey", ""]
        self.deleter.delete()
        self.assertEqual(2, len(self.io.outputs))

    def test_delete_reference_cancel(self):
        self.io.inputs = [""]
        self.deleter.delete()
        self.assertAlmostEqual(1, len(self.io.outputs))