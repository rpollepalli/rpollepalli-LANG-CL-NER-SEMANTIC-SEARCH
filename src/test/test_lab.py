from src.main.lab import create_ner_pipeline, get_Bass_Pro_Shop_company_document, get_George_going_to_dinner_document, get_George_Washington_Document
import unittest

class TestNERSearch(unittest.TestCase):
    def test_create_ner_pipeline(self):
        self.assertIsNotNone(type(create_ner_pipeline()))

    def test_get_Bass_Pro_Shop_company_document(self):
        self.assertEqual(get_Bass_Pro_Shop_company_document(), [["3"], ["Bass Pro Shop has a new offering: weather resistant sneakers!"]])

    def test_get_George_going_to_dinner_document(self):
        self.assertEqual(get_George_going_to_dinner_document(), [["5"], ["I took George to Washington so we could have dinner at his favorite resturant."]])

    def test_get_George_Washington_Document(self):
        self.assertEqual(get_George_Washington_Document(), [["6"], ["According to my research, George Washington and Napoleon Bonaparte never met"]])
        
if __name__ == '__main__':
    unittest.main()