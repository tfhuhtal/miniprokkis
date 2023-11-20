import json
import os


class Converter:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.json_data = self._load_json()

    def convert(self):
        """Converts json data to string."""

        return json.dumps(self.json_data)

    def _load_json(self):
        """Loads json data from file. If file does not exist, creates new one with default data."""

        if not os.path.isfile(self.json_file_path):
            print(
                f"File {self.json_file_path} does not exist. Creating new one with default data.")
            self._create_json_file()

        with open(self.json_file_path, "r") as f:
            return json.load(f)

    def _create_json_file(self):
        """Creates new json file with default data."""

        with open(self.json_file_path, "w") as f:
            f.write("{}")
