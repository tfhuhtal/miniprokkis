import json

class ReferenceTypes:
    def __init__(self, source_types_path):
        self._file_path = source_types_path
        self._source_types = self._load_json()

#Metodi palauttaa sanakirjan, jossa on avaimet "required" ja "optional", eli listat eri kentistä
    def get_fields(self, type):
        return self._source_types[type]
    
#lataa source_types.json
    def _load_json(self):
        with open(self.file_path, "r") as file:
            return json.load(file)