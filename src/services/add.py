# pylint: disable=R1705
import re
from assets.reference import Reference
from assets.reference_types import ReferenceTypes
from services.key import Keyhandler


class AddService:
    def __init__(self, converter, io):
        self.io = io
        self.converter = converter
        self.json_data = converter.return_data()
        self.reference_types = ReferenceTypes("src/assets/source_types.json")
        self.keyhandler = Keyhandler(converter)

    def add_reference(self, reference):
        reference_data = reference.to_json()
        self.json_data.append(reference_data)
        self.converter.save_json()

    def input_ref_key(self, existing_keys: list):
        while True:
            if len(self.io.inputs) == 0:  # pragma: no cover
                self.io.add_input(
                    "\nLähteen avain: ('Q' peruaksesi toiminto) ")
            input = self.io.read()

            if input == "Q":
                return 0

            if input in existing_keys:
                self.io.write(
                    f"\nAvain '{input}' on jo käytössä. Käytä jotain toista avainta.")
                continue

            if re.match("^[A-Za-z0-9_-]+$", input):
                return input
            self.io.write(
                "\nAvain saa sisältää vain kirjaimia a-z ja numeroita.")
            continue

    def input_ref_type(self, types: list):
        self.io.write("\nMahdolliset lähdetyypit:")

        for i in range(len(types)):
            self.io.write(f"{i + 1 : >2}. {types[i]}")

        while True:
            if len(self.io.inputs) == 0:  # pragma: no cover
                self.io.write(
                    "\nLähteen tyyppi: ('Q' peruaksesi toiminto) ")
                self.io.add_input(
                    "komento: ")
            input = self.io.read()

            if input == "Q":
                return 0

            if input.isdigit() and 1 <= int(input) <= len(types):
                return types[int(input) - 1]
            else:
                self.io.write(
                    f"\nVirhe: valitse lähdetyyppi numerolla 1-{len(types)}")

    def input_ref_fields(self, data: dict, fields: dict, field_type: str):
        self.io.write(f"\n{field_type} kentät: ('Q' peruaksesi toiminto) ")

        for field in fields[field_type]:
            while True:
                if len(self.io.inputs) == 0:  # pragma: no cover
                    self.io.add_input(f"{field : >12}: ")

                input = self.io.read()

                if input == "Q":
                    return 0

                if input == "" and field_type == "Pakolliset":
                    self.io.write("\nKenttä ei voi olla tyhjä")
                    continue
                if input == "" and field_type == "Vapaaehtoiset":
                    break

                validate_result = self.validate_input(input, field)
                if validate_result != 1:
                    self.io.write(f"Virhe: ({validate_result})")
                    continue

                data["fields"][field] = input
                break

        return 1

    def add(self):
        data = {}

        # Kysy lähteen avainta
        existing_keys = self.keyhandler.get_keys()

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
        self.add_reference(new_reference)
        self.io.write("\nLähde lisätty.")

    def validate_input(self, input, field: str):
        if field == "year" and not re.match(r"^\d{4}$", input):
            return "year-kentän tulee olla 4 numeroinen"
        if field == "pages" and not re.match(
                r"^\d+(--\d+)?(, \d+(--\d+)?)*$", input):
            return "pages-kentän tulee olla muotoa '1' tai '1--5' tai '1, 3--5, 7'"
        return 1
