from converter import Converter
from reference import Book

class ReferenceHandler:
    def __init__(self, io):
        self.converter = Converter("example.json")
        self.io = io

    def info(self):
        self.io.write("Komennot: ")
        self.io.write("0 Sulje sovellus")
        self.io.write("1 Lisää kirja")
        self.io.write("2 Tulosta viitelista")


    def add(self):
        key = self.io.read("Kirjan avain: ")
        title = self.io.read("Kirjan nimi: ")
        author = self.io.read("Kirjoittaja: ")
        year = self.io.read("Julkaisuvuosi: ")

        new_book = Book(key, author, title, year)
        self.converter.add_book(new_book)
        self.io.write("Kirja lisätty.")

    def list_references(self):
        self.io.write("Viitelista:")
        self.io.write(self.converter.convert())

    def run(self):
        self.info()
        while True:
            self.io.write("")
            command = self.io.read("Komento: ")
            if command == "0":
                break
            elif command == "1":
                self.add()
            elif command == "2":
                self.list_references()
            else:
                self.info()
