import json
import os


class Converter:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.json_data = self._load_json()

    def convert(self):
        """Converts json data to string."""

        return json.dumps(self.json_data)

    def get_keys(self):
        if (len(self.json_data) < 1):
            return []

        keys = []

        for i in range(len(self.json_data)):
            entry = self.json_data[i]
            keys.append(entry['key'])

        return keys

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

    def add_reference(self, reference):
        reference_data = reference.to_json()
        self.json_data.append(reference_data)
        self._save_json()

    def _save_json(self):
        """Saves the current state of JSON data back to the file."""
        with open(self.json_file_path, "w", encoding="utf-8") as f:
            json.dump(self.json_data, f, indent=4)

    def formatted_print(self):
        """Print existing reference catalogue to the console with pretty formatting."""

        if (len(self.json_data) < 1):
            return "Viitelistalle ei ole vielä lisätty yhtään viitettä!"

        title = f"Viitelista - yhteensä {len(self.json_data)} viite(ttä):"
        pretty_strings = [title]

        for i in range(len(self.json_data)):
            pretty_strings.append("")

            try:
                entry = self.json_data[i]
                entry_type = entry['type']
                entry_key = entry['key']
                entry_fields = entry['fields']

                full_row = f"Viite {i + 1} on tyypiltään '{entry_type}'."
                pretty_strings.append(full_row)

                full_row = f"Sen yksilöity avain on '{entry_key}'."
                pretty_strings.append(full_row)

                for keys in entry_fields:
                    full_row = f"{keys : >15}: {entry_fields[keys]}"
                    pretty_strings.append(full_row)

            except BaseException:
                return "Viitelistan lukemisessa esiintyi virhe. Listaa ei ole mahdollista tulostaa."

        return pretty_strings

    def delete_reference(self, reference_key):
        for i in range(len(self.json_data)):
            entry = self.json_data[i]
            entry_key = entry['key']
            if entry_key == reference_key:
                self.json_data.pop(i)
                self._save_json()
