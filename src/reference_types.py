import json

class ReferenceTypes:
    def __init__(self, source_types_path):
        self._file_path = source_types_path
        self._source_types = self._load_json()

# Metodi palauttaa sanakirjan, jossa on avaimet "Pakolliset" ja "Vapaaehtoiset",
# eli listat eri kentistä
    def get_fields(self, type):
        return self._source_types[type]

# Palauttaa listan eri lähdetyypeistä
    def get_types(self):
        return list(self._source_types.keys())

# lataa source_types.json
    def _load_json(self):
        with open(self._file_path, "r") as file: #pylint: disable=unspecified-encoding
            return json.load(file)
