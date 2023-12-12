# pylint: disable=E1121
from services.converter import Converter
from services.print import Printservice
from services.key import Keyhandler
from services.delete import DeleteService
from services.add import AddService
from services.recommend import Recommendation


class ServiceHandler:
    def __init__(self, io, converter=None):
        self.io = io
        self.converter = converter if converter else Converter(
            "savedreferences.json", self.io)
        self.printter = Printservice(self.converter, self.io)
        self.keyhandler = Keyhandler(self.converter)
        self.deletehandler = DeleteService(self.converter, self.io)
        self.adder = AddService(self.converter, self.io)
        self.recommendation = Recommendation(self.converter, self.io, self.keyhandler)

    def info(self):
        self.io.write("")
        self.io.write("Komennot:")
        self.io.write("  0   Sulje sovellus")
        self.io.write("  1   Lisää lähde")
        self.io.write("  2   Tulosta viitelista")
        self.io.write("      -a: aakkosjärjestyksessä")
        self.io.write("      -c: kompakti muoto")
        self.io.write("  3   Poista lähde")
        self.io.write("  4   Tulosta bibtex-lähdelista")
        self.io.write("      -f: tallenna tiedostoon")
        self.io.write("  5   Hae lähteistä")
        self.io.write("      -c: kompakti muoto")
        self.io.write("  6   Hae lähteistä avaimella")
        self.io.write("      -c: kompakti muoto")
        self.io.write("  7   Hae kirjasuositus")

    def run(self):
        self.info()
        while True:
            self.io.write("")
            if len(self.io.inputs) == 0:  # pragma: no cover
                self.io.add_input("komento: ")  # pragma: no cover
            command = self.io.read()
            if command == "0":
                break
            if command == "1":
                self.adder.add()
            if command == "2":
                self.printter.list_references(False, False)
            if command == "2 -a":
                self.printter.list_references(True, False)
            if command == "2 -c":
                self.printter.list_references(False, True)
            if command == "2 -a -c" or command == "2 -c -a":
                self.printter.list_references(
                    True, True)
            if command == "3":
                self.deletehandler.delete()
            if command == "4":
                self.printter.print_bibtex()
            if command == "4 -f":
                self.converter.bibtex_to_file()
            if command == "5":
                self.printter.search(False)
            if command == "5 -c":
                self.printter.search(True)
            if command == "6":
                self.printter.search_by_key(False)
            if command == "6 -c":
                self.printter.search_by_key(True)
            if command == "7":
                self.recommendation.get_rec()
                self.io.write("")
                self.info()
            if command == "":
                self.info()
  