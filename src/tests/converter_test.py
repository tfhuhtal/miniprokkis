import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter("exampl.json")

    def test_convert(self):
        self.assertEqual(self.converter.convert(), "{}")

    def test_formatted_printing(self):
        self.converter.json_data = [{'type': 'article',
                                     'key': 'Smith2019',
                                     'fields': {'author': 'John Smith',
                                                'title': 'A Sample Article',
                                                'journal': 'Journal of Samples',
                                                'year': '2019'}},
                                    {'type': 'book',
                                     'key': 'Doe2020',
                                     'fields': {'author': 'Jane Doe',
                                                'title': 'Introduction to Samples',
                                                'publisher': 'Sample Publishers',
                                                'year': '2020'}}]
        return_value = self.converter.formatted_print()
        self.assertEqual(15, len(return_value))
        self.assertEqual(
            "Viitelista - yhteensä 2 viite(ttä):",
            return_value[0])
        self.assertEqual("Sen yksilöity avain on 'Doe2020'.", return_value[10])

    def test_formatted_printing_error_handling(self):
        self.converter.json_data = [{'type': 'article',
                                     'key': 'Smith2019',
                                     'fields': {'author': 'John Smith',
                                                'title': 'A Sample Article',
                                                'year': '2019'}},
                                    {"virheellinen avain!!!": 'book',
                                     'key': 'Doe2020',
                                     'fields': {'author': 'Jane Doe',
                                                'title': 'Introduction to Samples',
                                                'publisher': 'Sample Publishers',
                                                'year': '2020'}}]
        return_value = self.converter.formatted_print()
        self.assertEqual(
            "Viitelistan lukemisessa esiintyi virhe. Listaa ei ole mahdollista tulostaa.",
            return_value)
