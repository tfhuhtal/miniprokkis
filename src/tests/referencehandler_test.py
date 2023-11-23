import unittest
from referencehandler import ReferenceHandler
from console_io import ConsoleIO

class TestReferenceHandler(unittest.TestCase):
    def setUp(self):
        io = ConsoleIO()
        self.handler = ReferenceHandler(io)

