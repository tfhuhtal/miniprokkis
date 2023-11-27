import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter("exampl.json")

    def test_convert(self):
        self.converter.json_data = []
        self.assertEqual(self.converter.convert(), "[]")

    def test_concerter_get_keys_empty(self):
        self.converter.json_data = []
        self.assertEqual(self.converter.get_keys(), [])

    def test_concerter_get_keys_with_keys(self):
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
        self.assertEqual(self.converter.get_keys(), ['Smith2019', 'Doe2020'])

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
        return_value = self.converter.formatted_print(False)
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
        return_value = self.converter.formatted_print(False)
        self.assertEqual(
            "Viitelistan lukemisessa esiintyi virhe. Listaa ei ole mahdollista tulostaa.",
            return_value)

    def test_delete_reference(self):
        self.converter.json_data = [{'type': 'article',
                                     'key': 'testi',
                                     'fields': {'author': 'John Smith',
                                                'title': 'A Sample Article',
                                                'journal': 'Journal of Samples',
                                                'year': '2019'}},
                                    {'type': 'article',
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
        self.converter.delete_reference('testi')
        self.assertEqual(self.converter.json_data, [{'type': 'article',
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
                                                'year': '2020'}}])
