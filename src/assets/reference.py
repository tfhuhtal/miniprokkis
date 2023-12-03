# pylint: skip-file 

class Reference:
    def __init__(self, data):
        self.data = data

    def to_json(self):
        return {
            "type": self.data["type"],
            "key": self.data["key"],
            "fields": self.data["fields"]
        }
