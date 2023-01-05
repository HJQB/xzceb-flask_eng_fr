import unittest

# Import the script containing the functions to be tested
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)
        self.assertEqual(englishToFrench('Thank you.'), 'Je vous remercie.')
        self.assertEqual(englishToFrench('Goodbye.'), 'Au revoir.')

    def test_frenchToEnglish(self):
        self.assertNotEqual(frenchToEnglish("None"), '')
        self.assertNotEqual(frenchToEnglish(0), 0)
        self.assertEqual(frenchToEnglish('Je vous remercie.'), 'Thank you.')
        self.assertEqual(frenchToEnglish('Au revoir.'), 'Goodbye.')

if __name__ == '__main__':
    unittest.main()
