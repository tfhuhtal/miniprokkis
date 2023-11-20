import json

class Converter:
    def __init__(self, json_file_path):
        self.json_data = json.load(open(json_file_path))

    
    def convert(self):
        return json.dumps(self.json_data)
        