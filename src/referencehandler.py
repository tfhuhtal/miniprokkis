import re
from converter import Converter
from reference import Reference
from reference_types import ReferenceTypes


class ReferenceHandler:
    def __init__(self, io, converter=None):
        self.converter = converter if converter else Converter("savedreferences.json")
        self.io = io
        self.reference_types = ReferenceTypes("src/assets/source_types.json")

    def info(self):
        self.io.write("Komennot: ")
        self.io.write("0 - Sulje sovellus")
        self.io.write("1 - Lisää lähde")
        self.io.write("2 - Tulosta viitelista (-a aakkosjärjestyksessä)")
        self.io.write("3 - Poista lähde")
        self.io.write("4 - Tulosta bibtex -lähdelista")

    def input_ref_key(self, existing_keys: list):
        while True:        
            if len(self.io.inputs) == 0:
                self.io.add_input("\nLähteen avain: ('ENTER' peruaksesi toiminto) ")
            input = self.io.read()
            
            if input == "":
                return 0

            if input in existing_keys:
                self.io.write(
                    f"\nAvain '{input}' on jo käytössä. Käytä jotain toista avainta.")
                continue

            if re.match("^[A-Za-z0-9_-]+$", input):
                return input
            self.io.write(
                    f"\nAvain saa sisältää vain kirjaimia a-z ja numeroita.")
            continue


    def input_ref_type(self, types: list):
        self.io.write(
            f"\nMahdolliset lähdetyypit: {self._string_of_types(types)}")

        while True:
            if len(self.io.inputs) == 0:
                self.io.add_input("\nLähteen tyyppi: ('exit' peruaksesi toiminto) ")
            input = self.io.read()

            if input == "":
                self.io.write("\nKenttä ei voi olla tyhjä")
                continue

            if input == "exit":
                return 0

            if input not in types:
                self.io.write("\nTyyppi ei käytössä")
                continue

            return input

    def input_ref_fields(self, data: dict, fields: dict, field_type: str):
        self.io.write(f"\n{field_type} kentät: ('exit' peruaksesi toiminto) ")
        for field in fields[field_type]:
            while True:
                if len(self.io.inputs) == 0:
                    self.io.add_input(f"{field : >12}: ")
                input = self.io.read()
                if input == "exit":
                    return 0
                validate_result = self.validate_input(input, field)
                if input != "":
                    if validate_result != 1:
                        self.io.write(f"Virhe: ({validate_result})")
                        continue
                if input == "" and field_type == "Pakolliset":
                    self.io.write("\nKenttä ei voi olla tyhjä")
                    continue
                else:
                    break
            if input != "":
                data["fields"][field] = input
        return 1

    def add(self):
        data = {}

        # Kysy lähteen avainta
        existing_keys = self.converter.get_keys()

        input = self.input_ref_key(existing_keys)
        if input == 0:
            self.io.write("\nToiminto peruttu")
            return 0
        data["key"] = input

        # Kysy lähteen tyyppiä, jonka pitää löytyä source_types.json
        # tiedostosta
        types = self.reference_types.get_types()
        input = self.input_ref_type(types)
        if input == 0:
            self.io.write("\nToiminto peruttu")
            return 0
        data["type"] = input

        # Hae pakolliset ja vapaaehtoiset kentät lähdetyypin perusteella
        data["fields"] = {}
        fields = self.reference_types.get_fields(data["type"])

        # Kysy pakolliset kentät
        if self.input_ref_fields(data, fields, "Pakolliset") == 0:
            self.io.write("\nToiminto peruttu")
            return 0

        # Kysy vapaaehtoiset kentät. Tyhjä input ohittaa kentän
        if self.input_ref_fields(data, fields, "Vapaaehtoiset") == 0:
            self.io.write("\nToiminto peruttu")
            return 0

        new_reference = Reference(data)
        self.converter.add_reference(new_reference)
        self.io.write("\nLähde lisätty.")

    def list_references(self, alphabetical):
        data = self.converter.formatted_print(alphabetical)

        for entry in data:
            self.io.write(entry)

    def delete(self):
        # Kysy lähteen avainta
        key = ""
        while True:
            if len(self.io.inputs) == 0:
                self.io.add_input("\nLähteen avain: ('ENTER' peruaksesi toiminto) ")
            input = self.io.read()
            if input == "":
                self.io.write("\nToiminto peruttu")
                return
            key = input
            existing_keys = self.converter.get_keys()
            if key not in existing_keys:
                self.io.write("\nLähdettä ei voitu poistaa. Tarkista avain.")
            else:
                self.converter.delete_reference(key)
                self.io.write("\nLähde poistettu.")
                return           

    def run(self):
        self.info()
        while True:
            self.io.write("")
            if len(self.io.inputs) == 0:
                self.io.add_input("komento: ")
            command = self.io.read()
            if command == "0":
                break
            elif command == "1":
                self.add()
            elif command == "2":
                self.list_references(False)
            elif command == "2 -a":
                self.list_references(True)
            elif command == "3":
                self.delete()
            elif command == "4":
                self.print_bibtex()
            else:
                self.info()

    def _string_of_types(self, types):
        string = ""
        for type in types:
            string += type + " "
        return string
    
    def print_bibtex(self):
        data = self.converter.convert_json_to_bibtex()
        self.io.write("\nViitelista bibtex muodossa:\n")
        self.io.write(data)

    def validate_input(self, input, field: str):
        if field == "year" and not re.match(r"^\d{4}$", input):
            return "year-kentän tulee olla 4 numeroinen"
        if field == "pages" and not re.match(r"^\d+(--\d+)?(, \d+(--\d+)?)*$", input):
            return "pages-kentän tulee olla muotoa '1' tai '1--5' tai '1, 3--5, 7'"
        return 1
