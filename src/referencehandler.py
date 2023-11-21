from converter import Converter
from reference import Book

class ReferenceHandler:
    def __init__(self):
        self.converter = Converter("example.json")

    def info(self):
        print("Komennot: ")
        print("0 Sulje sovellus")
        print("1 Lisää kirja")
        print("2 Tulosta viitelista")


    def add(self):
        key = input("Kirjan avain: ")
        title = input("Kirjan nimi: ")
        author = input("Kirjoittaja: ")
        year = input("Julkaisuvuosi: ")

        new_book = Book(key, author, title, year)
        self.converter.add_book(new_book)
        print("Kirja lisätty.")

    def list_references(self):
        print("Viitelista:")
        print(self.converter.convert())

    def run(self):
        self.info()
        while True:
            print("")
            command = input("Komento: ")
            if command == "0":
                break
            elif command == "1":
                self.add()
            elif command == "2":
                self.list_references()
            else:
                self.info()
