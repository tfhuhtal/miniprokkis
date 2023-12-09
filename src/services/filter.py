class FilterService:
    def search(self, data, word):
        if word in data:
            return data[word]
