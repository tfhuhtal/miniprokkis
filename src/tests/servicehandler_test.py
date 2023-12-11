# pylint: skip-file
import unittest
from servicehandler import ServiceHandler


class ConverterStub:
    def __init__(self, json_file_path, io):
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
        self.io = io

    def get_keys(self):
        return [entry['key'] for entry in self.json_data]

    def add_reference(self, reference):
        self.json_data.append(reference.to_json())

    def delete_reference(self, reference_key):
        self.json_data = [
            entry for entry in self.json_data if entry['key'] != reference_key]

    def return_data(self):
        return self.json_data

    def convert_json_to_bibtex(self):
        return "Bibtex muotoisia viitteitä"

    def bibtex_to_file(self):
        self.io.write(f"Uusi .bib viitetiedosto luotu nimellä references.bib")


class ConsoleIOStub:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)
        print(value)

    def read(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def add_input(self, value, val=False):
        if not val:
            self.inputs.append(input(value))
        else:
            self.inputs.append(value)


class TestServiceHandler(unittest.TestCase):
    def setUp(self):
        self.io_stub = ConsoleIOStub()
        self.converter_stub = ConverterStub('testi', self.io_stub)
        self.handler = ServiceHandler(self.io_stub, self.converter_stub)

    def test_info(self):
        self.handler.info()
        expected_outputs = [
            "Komennot:",
            "  0   Sulje sovellus",
            "  1   Lisää lähde",
            "  2   Tulosta viitelista",
            "      -a: aakkosjärjestyksessä",
            "      -c: kompakti muoto",
            "  3   Poista lähde",
            "  4   Tulosta bibtex-lähdelista",
            "      -f: tallenna tiedostoon",
            "  5   Hae lähteistä",
            "      -c: kompakti muoto"
        ]
        self.assertEqual(self.io_stub.outputs, expected_outputs)

    def test_run_and_exit(self):
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn("Komennot:", self.io_stub.outputs)

    def test_run_and_add(self):
        self.io_stub.add_input("1", True)
        self.io_stub.add_input("Q", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn("\nToiminto peruttu", self.io_stub.outputs)

    def test_run_and_print(self):
        self.io_stub.add_input("2", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn(
            "Viitelista:",
            self.io_stub.outputs)

    def test_run_and_print_a(self):
        self.io_stub.add_input("2 -a", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn("Viitelista aakkosjärjestyksessä:",
                      self.io_stub.outputs)

    def test_run_and_print_c(self):
        self.io_stub.add_input("2 -c", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn("Tiiviissä muodossa:",
                      self.io_stub.outputs)

    def test_run_and_print_a_c(self):
        self.io_stub.add_input("2 -a -c", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn(
            "Viitelista aakkosjärjestyksessä:",
            self.io_stub.outputs)
        self.assertIn("Tiiviissä muodossa:",
                      self.io_stub.outputs)

    def test_run_and_delete(self):
        self.io_stub.add_input("3", True)
        self.io_stub.add_input("Martin2000", True)
        self.io_stub.add_input("", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn("\nLähdettä ei voitu poistaa. Tarkista avain.",
                      self.io_stub.outputs)

    def test_run_and_print_bibtex(self):
        self.io_stub.add_input("4", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn("\nViitelista bibtex muodossa:\n", self.io_stub.outputs)

    def test_run_and_bibtex_to_file(self):
        self.io_stub.add_input("4 -f", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn("Uusi .bib viitetiedosto luotu nimellä references.bib",
                      self.io_stub.outputs)

    def test_run_and_search(self):
        self.io_stub.add_input("5", True)
        self.io_stub.add_input("Johnson", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn(
            "Viite 'John2020' on tyypiltään 'book'.",
            self.io_stub.outputs)

    def test_run_and_search_c(self):
        self.io_stub.add_input("5 -c", True)
        self.io_stub.add_input("Johnson", True)
        self.io_stub.add_input("0", True)
        self.handler.run()
        self.assertIn("Tiiviissä muodossa:", self.io_stub.outputs)
