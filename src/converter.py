import json

class Converter:
    def __init__(self, json_data):
        self.json_data = json_data
    
    def convert(self):
        return json.dumps(self.json_data)
        