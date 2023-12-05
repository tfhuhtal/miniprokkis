class Printservice:
    def __init__(self, converter, io):
        self.converter = converter
        self.json_data = converter.return_data()
        self.io = io

    def formatted_print(self, alphabetical, compact):
        """Print existing reference catalogue to the console with pretty formatting."""
        try:
            if len(self.json_data) < 1:
                return "Viitelistalle ei ole vielä lisätty yhtään viitettä!"
        except BaseException:
            return "Viitelistan lukemisessa esiintyi virhe. Listaa ei ole mahdollista tulostaa."
        if alphabetical:
            title = f"Viitelista aakkosjärjestyksessä - yhteensä {len(self.json_data)} viite(ttä):"
        elif compact:
            title = f"Tiivis viitelista - yhteensä {len(self.json_data)} viite(ttä):"
        else:
            title = f"Viitelista - yhteensä {len(self.json_data)} viite(ttä):"

        pretty_strings = [title]

        all_authors = self.get_authors()
        final_list = ["None"] * len(self.get_keys())

        if alphabetical is True:
            all_authors = sorted(all_authors, key=str.casefold)

        for i in range(len(self.json_data)):
            this_entry = []
            this_entry.append("")

            try:
                entry = self.json_data[i]
                entry_type = entry['type']
                entry_key = entry['key']
                entry_fields = entry['fields']

                full_row = f"Viite '{entry_key}' on tyypiltään '{entry_type}'."
                this_entry.append(full_row)

                if compact is True:
                    compact_line = ""

                for keys in entry_fields:
                    if compact is True:
                        if len(entry_fields[keys]) > 20:
                            compact_line = compact_line + f"{keys}: {entry_fields[keys][:17]}...; "
                        else:
                            compact_line = compact_line + f"{keys}: {entry_fields[keys]}; "

                    else:
                        full_row = f"{keys : >15}: {entry_fields[keys]}"
                        this_entry.append(full_row)

                if compact is True:
                    this_entry.append(compact_line)

                target_index = all_authors.index(entry_fields['author'])

                if alphabetical is True:
                    while True:
                        if final_list[target_index] == "None":
                            final_list[target_index] = this_entry
                            break
                        target_index += 1
                else:
                    final_list[i] = this_entry

            except BaseException:
                return "Viitelistan tulostuksessa esiintyi virhe. Listaa ei ole mahdollista tulostaa."

        for entry in final_list:
            for line in entry:
                pretty_strings.append(line)

        return pretty_strings

    def get_authors(self):
        authors = []

        for i in range(len(self.json_data)):
            entry = self.json_data[i]
            authors.append(entry['fields']['author'])

        return authors

    def get_keys(self):
        keys = []

        for i in range(len(self.json_data)):
            entry = self.json_data[i]
            keys.append(entry['key'])

        return keys

    def print_bibtex(self):
        data = self.converter.convert_json_to_bibtex()
        self.io.write("\nViitelista bibtex muodossa:\n")
        self.io.write(data)

    def list_references(self, alphabetical, compact):
        data = self.formatted_print(alphabetical, compact)

        for entry in data:
            self.io.write(entry)
