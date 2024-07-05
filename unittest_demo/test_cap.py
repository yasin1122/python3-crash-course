"""
This is the test script for cap.py
"""

# import statements
import unittest
import cap

class TestCap(unittest.TestCase):
    """
    Contains functions to test cap.py
    """

    def test_one_word(self):
        """
        Tests cap_text with one word.
        """
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        """
        Tests cap_text with multiple words.
        """
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
