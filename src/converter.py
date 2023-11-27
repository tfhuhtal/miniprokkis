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

    def formatted_print(self, alphabetical):
        """Print existing reference catalogue to the console with pretty formatting."""

        if (len(self.json_data) < 1):
            return "Viitelistalle ei ole vielä lisätty yhtään viitettä!"

        title = f"Viitelista - yhteensä {len(self.json_data)} viite(ttä):"
        pretty_strings = [title]

        if alphabetical == True:
            all_keys = self.get_keys()
            all_keys.sort()

            for i in range(len(all_keys)):
                this_entry = []
                this_entry.append("")

                try:
                    entry = self.json_data[i]
                    entry_type = entry['type']
                    entry_key = entry['key']
                    entry_fields = entry['fields']

                    full_row = f"Viite {i + 1} on tyypiltään '{entry_type}'."
                    this_entry.append(full_row)

                    full_row = f"Sen yksilöity avain on '{entry_key}'."
                    this_entry.append(full_row)

                    for keys in entry_fields:
                        full_row = f"{keys : >15}: {entry_fields[keys]}"
                        this_entry.append(full_row)
                    
                    target_index = all_keys.index(entry_key)

                    all_keys[target_index] = this_entry

                except BaseException:
                    return "Viitelistan lukemisessa esiintyi virhe. Listaa ei ole mahdollista tulostaa."
            
            for entry in all_keys:
                for line in entry:
                    pretty_strings.append(line)
        
            return pretty_strings

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
                return

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
