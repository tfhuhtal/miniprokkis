import json
import os


class Converter:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.json_data = self._load_json()

    def convert(self):
        """Converts json data to string."""

        return json.dumps(self.json_data)

    def return_data(self):
        return self.json_data

    def _load_json(self):
        """Loads json data from file. If file does not exist, creates new one with default data."""

        if not os.path.isfile(self.json_file_path):
            print(
                f"File {self.json_file_path} does not exist. Creating new one with default data.")
            self._create_json_file()

        with open(self.json_file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _create_json_file(self):
        """Creates new json file with default data."""

        with open(self.json_file_path, "w", encoding="utf-8") as f:
            f.write("{}")

    def save_json(self):
        """Saves the current state of JSON data back to the file."""
        with open(self.json_file_path, "w", encoding="utf-8") as f:
            json.dump(self.json_data, f, indent=4)

    def convert_json_to_bibtex(self):
        self.bibtex_entries = []
        for entry in self.json_data:
            bibtex_entry = self._create_bibtex_entry(entry)
            self.bibtex_entries.append(bibtex_entry)

        return "\n".join(self.bibtex_entries)

    def _create_bibtex_entry(self, entry):
        bibtex_entry = f"@{entry['type']}{{{entry['key']}}},\n"

        for field, value in entry['fields'].items():
            bibtex_entry += f"  {field} = {{{value}}},\n"

        bibtex_entry = bibtex_entry.rstrip(",\n") + "\n"
        bibtex_entry += "}\n"

        return bibtex_entry
