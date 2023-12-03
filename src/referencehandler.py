from converter import Converter
from services.print.printservice import Printservice
from services.keyhandler import Keyhandler
from services.delete import DeleteService
from services.add import AddService


class ReferenceHandler:
    def __init__(self, io, converter=None):
        self.converter = converter if converter else Converter(
            "savedreferences.json")
        self.io = io
        self.printter = Printservice(self.converter)
        self.keyhandler = Keyhandler(self.converter)
        self.deletehandler = DeleteService(self.converter)
        self.adder = AddService(self.converter)

    # siirrä
    def info(self):
        self.io.write("Komennot: ")
        self.io.write("0 - Sulje sovellus")
        self.io.write("1 - Lisää lähde")
        self.io.write("2 - Tulosta viitelista (-a aakkosjärjestyksessä)")
        self.io.write("3 - Poista lähde")
        self.io.write("4 - Tulosta bibtex -lähdelista")

    # siirrä

    # siirrä

    # siirrä

    # siirrä

    def list_references(self, alphabetical):
        data = self.printter.formatted_print(alphabetical)

        for entry in data:
            self.io.write(entry)

    # siirrä
    def delete(self):
        # Kysy lähteen avainta
        key = ""
        while True:
            if len(self.io.inputs) == 0:
                self.io.add_input(
                    "\nLähteen avain: ('ENTER' peruaksesi toiminto) ")
            input = self.io.read()
            if input == "":
                self.io.write("\nToiminto peruttu")
                return
            key = input
            existing_keys = self.keyhandler.get_keys()
            if key not in existing_keys:
                self.io.write("\nLähdettä ei voitu poistaa. Tarkista avain.")
            else:
                self.deletehandler.delete_reference(key)
                self.io.write("\nLähde poistettu.")
                return

    # siirrä
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
                self.list_references(False)
            if command == "2 -a":
                self.list_references(True)
            if command == "3":
                self.delete()
            if command == "4":
                self.print_bibtex()
            else:
                self.info()

    # siirrä

    # siirrä
    def print_bibtex(self):
        data = self.converter.convert_json_to_bibtex()
        self.io.write("\nViitelista bibtex muodossa:\n")
        self.io.write(data)

    # siirrä
