import unittest
from Task3 import concatenate_nth_letters

class TestConcatenateNthLetters(unittest.TestCase):
    def test_example_case_1(self):
        words = ["apple", "banana", "cherry"]
        self.assertEqual(concatenate_nth_letters(words), "aae")

    def test_example_case_2(self):
        words = ["dog", "elephant", "iguana", "octopus"]
        self.assertEqual(concatenate_nth_letters(words), "dluo")

    def test_empty_array(self):
        words = []
        self.assertEqual(concatenate_nth_letters(words), "")

    def test_single_word(self):
        words = ["hello"]
        self.assertEqual(concatenate_nth_letters(words), "h")

    def test_different_lengths(self):
        words = ["a", "bb", "ccc", "dddd"]
        self.assertEqual(concatenate_nth_letters(words), "abcd")

    def test_mixed_empty_and_non_empty_strings(self):
        words = ["", " b", "", "   d"]
        self.assertEqual(concatenate_nth_letters(words), "bd")

    def test_long_words(self):
        words = ["supercalifragilisticexpialidocious", "pneumonoultramicroscopicsilicovolcanoconiosis"]
        self.assertEqual(concatenate_nth_letters(words), "sn")

if __name__ == '__main__':
    unittest.main()