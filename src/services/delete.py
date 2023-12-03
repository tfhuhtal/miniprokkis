class DeleteService:
    def __init__(self, converter):
        self.converter = converter
        self.json_data = converter.return_data()
    
    def delete_reference(self, reference_key):
        for i in range(len(self.json_data)):
            entry = self.json_data[i]
            entry_key = entry['key']
            if entry_key == reference_key:
                self.json_data.pop(i)
                self.converter.save_json()
                return