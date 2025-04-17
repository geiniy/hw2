import unittest
from main import boyer_moore_search

class TestBoyerMoore(unittest.TestCase):

    def test_empty_pattern(self):
        self.assertEqual(boyer_moore_search("abc", ""), 0)

    def test_exact_match(self):
        self.assertEqual(boyer_moore_search("hello", "hello"), 0)

    def test_pattern_at_start(self):
        self.assertEqual(boyer_moore_search("abcdef", "abc"), 0)

    def test_pattern_at_end(self):
        self.assertEqual(boyer_moore_search("abcdef", "def"), 3)

    def test_pattern_in_middle(self):
        self.assertEqual(boyer_moore_search("abcXYZdef", "XYZ"), 3)

    def test_pattern_not_found(self):
        self.assertEqual(boyer_moore_search("abcdef", "gh"), -1)

    def test_pattern_longer_than_text(self):
        self.assertEqual(boyer_moore_search("abc", "abcdef"), -1)

    def test_multiple_occurrences(self):
        self.assertEqual(boyer_moore_search("abcabcabc", "abc"), 0)

    def test_single_char_match(self):
        self.assertEqual(boyer_moore_search("xyz", "y"), 1)

    def test_single_char_no_match(self):
        self.assertEqual(boyer_moore_search("xyz", "a"), -1)

    def test_repeated_chars(self):
        self.assertEqual(boyer_moore_search("aaaaaa", "aaa"), 0)

    def test_shift_logic(self):
        self.assertEqual(boyer_moore_search("ababcababcabc", "abcabc"), 7)