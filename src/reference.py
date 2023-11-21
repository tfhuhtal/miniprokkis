class Book:
    def __init__(self, key, author, title, year):
        self.key = key
        self.author = author
        self.title = title
        self.year = year
        self.type = 'book'

    def to_json(self):
        return {
            "type": self.type,
            "key": self.key,
            "fields": {
                "author": self.author,
                "title": self.title,
                "year": self.year
            }
        }
