from openai import OpenAI

class Recommendation:
    def __init__(self, converter, io, keyhandler):
        self.converter = converter
        self.io = io
        self.keyhandler = keyhandler
        self.json_data = converter.return_data()

    def get_rec(self):
        key = ""
        while True:
            if len(self.io.inputs) == 0:  # pragma: no cover
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
                for i in range(len(self.json_data)):
                    if input.lower() in str(self.json_data[i]["key"]).lower():
                        book = self.json_data[i]
                prompt_text = f"Give me a book recommendation based on the following book: {book['fields']['title']}, {book['fields']['author']}. Just the books name is enough."
                response = self.send_prompt(prompt_text)
                print("Kirjasuositus:", f"'{response}'")

    def send_prompt(self, prompt):
        with open('src/assets/api_key.txt', 'r') as file:
            api_key = file.read().strip()
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(model="gpt-3.5-turbo",  # Specify the model you want to use
            messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
            ],
            max_tokens=50)
            return response.choices[0].message.content if response.choices else "No response"
