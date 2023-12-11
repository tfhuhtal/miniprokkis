class Printservice:
    def __init__(self, converter, io):
        self.converter = converter
        self.json_data = converter.return_data()
        self.io = io

    def print(self, entry):
        entry_type = entry['type']
        entry_key = entry['key']
        entry_fields = entry['fields']
        full_row = f"Viite '{entry_key}' on tyypiltään '{entry_type}'."
        self.io.write(full_row)

        for keys in entry_fields:
            full_row = f"{keys : >15}: {entry_fields[keys]}"
            self.io.write(full_row)
        self.io.write("")

    def compact_print(self, entry):
        compact_line = ""
        entry_type = entry['type']
        entry_key = entry['key']
        entry_fields = entry['fields']

        required_fields = ['author', 'title', 'year']

        for keys in required_fields:
            if len(entry_fields[keys]) > 20:  # pragma: no cover
                compact_line = compact_line + \
                    f"{entry_fields[keys][:17]}..;"
            else:
                compact_line = compact_line + \
                    f"{entry_fields[keys] : <20}"
        self.io.write(f"{entry_key : <20}{entry_type : <16}{compact_line}")
        self.io.write("")

    def list_handler(self, compact, printdata):
        printlist = printdata
        if compact is True:
            self.io.write("Tiiviissä muodossa:")
            self.io.write(f"{'key' : <20}{'type' : <16}{'author' : <20}{'title' : <20}{'year'}")
        for i in range(len(printlist)):
            entry = printlist[i]
            if compact is True:
                self.compact_print(entry)
            else:
                self.print(entry)

    def list_references(self, alphabetical, compact):
        data = self.json_data
        if alphabetical is True:
            self.io.write("Viitelista aakkosjärjestyksessä:")
            self.sort_by_author(compact)
        else:
            self.io.write("Viitelista:")
            self.list_handler(compact, data)

    def print_bibtex(self):
        data = self.converter.convert_json_to_bibtex()
        self.io.write("\nViitelista bibtex muodossa:\n")
        self.io.write(data)

    def search(self, compact):
        if len(self.io.inputs) == 0:    # pragma: no cover
            self.io.add_input(
                "\nHakusana: ")
        word = self.io.read()

        results = []

        for i in range(len(self.json_data)):
            if word.lower() in str(self.json_data[i]['fields']).lower():
                results.append(self.json_data[i])
        self.list_handler(compact, results)

    def sort_by_author(self, compact):
        authors = sorted(self.get_authors(), key=lambda x: x[1])
        alphabeticallist = []

        for pair in authors:
            for i in range(len(self.json_data)):
                if pair[0] == str(self.json_data[i]['key']):
                    alphabeticallist.append(self.json_data[i])

        self.list_handler(compact, alphabeticallist)

    def get_authors(self):
        authors = []

        for i in range(len(self.json_data)):
            key_author = []
            entry = self.json_data[i]
            key_author.append(entry['key'])
            key_author.append(entry['fields']['author'])
            authors.append(key_author)

        return authors
