# pylint: skip-file
import unittest
from unittest.mock import Mock
from services.delete import DeleteService
from services.console_io import ConsoleIO

class TestDeleteService(unittest.TestCase):
    def setUp(self):
        self.converter = Mock()
        self.converter.return_data.return_value = []
        self.io = ConsoleIO()
        self.delete_service = DeleteService(self.converter, self.io)

#    def test_delete_reference(self):