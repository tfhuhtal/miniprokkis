class Keyhandler:
    def __init__(self, converter):
        self.json_data = converter.return_data()

    def get_keys(self):
        if len(self.json_data) < 1:
            return []

        keys = []

        for i in enumerate(self.json_data):
            entry = self.json_data[i]
            keys.append(entry['key'])

        return keys
