class AddService:
    def __init__(self, converter):
        self.converter = converter
        self.json_data = converter.return_data()

    def add_reference(self, reference):
        reference_data = reference.to_json()
        self.json_data.append(reference_data)
        self.converter.save_json()