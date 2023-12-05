from services.converter import Converter
from services.print.print import Printservice
from services.key import Keyhandler
from services.delete import DeleteService
from services.add import AddService


class ServiceHandler:
    def __init__(self, io, converter=None):
        self.io = io
        self.converter = converter if converter else Converter(
            "savedreferences.json", self.io)
        self.printter = Printservice(self.converter, self.io)
        self.keyhandler = Keyhandler(self.converter)
        self.deletehandler = DeleteService(self.converter, self.io)
        self.adder = AddService(self.converter, self.io)

    def info(self):
        self.io.write("Komennot: ")
        self.io.write("0 - Sulje sovellus")
        self.io.write("1 - Lisää lähde")
        self.io.write("2 - Tulosta viitelista (-a aakkosjärjestyksessä) (-c kompakti muoto)")
        self.io.write("3 - Poista lähde")
        self.io.write("4 - Tulosta bibtex -lähdelista (-f tiedostoon)")

    def run(self):
        self.info()
        while True:
            self.io.write("")
            if len(self.io.inputs) == 0:
                self.io.add_input("komento: ")
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
                self.printter.list_references(True, True)
            if command == "3":
                self.deletehandler.delete()
            if command == "4":
                self.printter.print_bibtex()
            if command == "4 -f":
                self.converter.bibtex_to_file()
            else:
                self.info()
