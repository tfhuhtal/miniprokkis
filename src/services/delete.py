from services.key import Keyhandler


class DeleteService:
    def __init__(self, converter, io):
        self.converter = converter
        self.json_data = converter.return_data()
        self.io = io
        self.keyhandler = Keyhandler(converter)

    def delete_reference(self, reference_key):
        for i in enumerate(self.json_data):
            entry = self.json_data[i]
            entry_key = entry['key']
            if entry_key == reference_key:
                self.json_data.pop(i)
                self.converter.save_json()
                return

    def delete(self):
        # Kysy lähteen avainta
        key = ""
        while True:
            if len(self.io.inputs) == 0:
                self.io.add_input(
                    "\nLähteen avain: ('ENTER' peruaksesi toiminto) ")
            input = self.io.read()
            if input == "":
                self.io.write("\nToiminto peruttu")
                return
            key = input
            existing_keys = self.keyhandler.get_keys()
            if key not in existing_keys:
                self.io.write("\nLähdettä ei voitu poistaa. Tarkista avain.")
            else:
                self.delete_reference(key)
                self.io.write("\nLähde poistettu.")
                return
