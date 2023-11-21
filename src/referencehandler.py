from converter import Converter
from reference import Reference
from reference_types import ReferenceTypes


class ReferenceHandler:
    def __init__(self, io):
        self.converter = Converter("example.json")
        self.io = io
        self.reference_types = ReferenceTypes("source_types.json")

    def info(self):
        self.io.write("Komennot: ")
        self.io.write("0 - Sulje sovellus")
        self.io.write("1 - Lisää lähde")
        self.io.write("2 - Tulosta viitelista")
        self.io.write("3 - Poista lähde")

    def add(self):
        data = {}

        # Kysy lähteen avainta
        while True:
            input = self.io.read(
                "\nLähteen avain: ('exit' peruaksesi toiminto) ")
            if input == "":
                self.io.write("\nKenttä ei voi olla tyhjä")
                continue
            if input == "exit":
                self.io.write("\nToiminto peruttu")
                return
            data["key"] = input
            break

        types = self.reference_types.get_types()

        # Kysy lähteen tyyppiä, jonka pitää löytyä source_types.json
        # tiedostosta
        self.io.write(
            f"\nMahdolliset lähdetyypit: {self._string_of_types(types)}")
        while True:
            input = self.io.read(
                "\nLähteen tyyppi: ('exit' peruaksesi toiminto) ")
            if input == "":
                self.io.write("\nKenttä ei voi olla tyhjä")
                continue
            if input == "exit":
                self.io.write("\nToiminto peruttu")
                return
            if input not in types:
                self.io.write("\nTyyppi ei käytössä")
                continue
            data["type"] = input
            break

        data["fields"] = {}
        # Hae pakolliset ja vapaaehtoiset kentät lähdetyypin perusteella
        fields = self.reference_types.get_fields(data["type"])

        # Kysy pakolliset kentät
        self.io.write("\nPakolliset kentät: ('exit' peruaksesi toiminto) ")
        for field in fields["required"]:
            while True:
                input = self.io.read(f"{field}: ")
                if input == "exit":
                    self.io.write("\nToiminto peruttu")
                    return
                if input == "":
                    self.io.write("\nKenttä ei voi olla tyhjä")
                    continue
                data["fields"][field] = input
                break

        # Kysy vapaaehtoiset kentät. Tyhjä input ohittaa kentän
        self.io.write(
            "\nVapaaehtoiset kentät: ('exit' peruaksesi toiminto, ENTER = seuraava kenttä) ")
        for field in fields["optional"]:
            while True:
                input = self.io.read(f"{field}: ")
                if input == "exit":
                    self.io.write("\nToiminto peruttu")
                    return
                if input == "":
                    break
                data["fields"][field] = input
                break

        new_reference = Reference(data)
        self.converter.add_reference(new_reference)
        self.io.write("\nLähde lisätty.")

    def list_references(self):
        data = self.converter.formatted_print()

        for entry in data:
            self.io.write(entry)
            
    def delete(self):
        # Kysy lähteen avainta
        key = ""
        while True:
            input = self.io.read(
                "\nLähteen avain: ('exit' peruaksesi toiminto) ")
            if input == "":
                self.io.write("\nKenttä ei voi olla tyhjä")
                continue
            if input == "exit":
                self.io.write("\nToiminto peruttu")
                return
            key = input
            self.converter.delete_reference(key)
            self.io.write("\nLähde poistettu.")                	

    def run(self):
        self.info()
        while True:
            self.io.write("")
            command = self.io.read("Komento: ")
            if command == "0":
                break
            elif command == "1":
                self.add()
            elif command == "2":
                self.list_references()
            elif command == "3":
                self.delete()
            else:
                self.info()

    def _string_of_types(self, types):
        string = ""
        for type in types:
            string += type + " "
        return string
