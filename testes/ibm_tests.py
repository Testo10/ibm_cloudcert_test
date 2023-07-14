from deep_translator import MyMemoryTranslator
import unittest

class TranslationTestCase(unittest.TestCase):

    def setUp(self):
        self.translator = MyMemoryTranslator(source='fr-FR', target='en-US')

    def test_french_to_english_translation(self):
        self.assertEqual(self.translator.translate("Bonjour"), "Hi")

    def test_french_to_english_translation_not_equal(self):
        self.assertNotEqual(self.translator.translate("Bonjour"), "Bonjour")

class TranslationTestCase2(unittest.TestCase):

    def setUp(self):
        self.translator = MyMemoryTranslator(source='en-US', target='fr-FR')

    def test_english_to_french_translation(self):
        self.assertEqual(self.translator.translate("Hello"), "Bonjour")

    def test_english_to_french_translation_not_equal(self):
        self.assertNotEqual(self.translator.translate("Hello"), "Hello")

if __name__ == '__main__':
    unittest.main()

