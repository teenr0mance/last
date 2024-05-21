import unittest
from reverse import reverse

class TestReverse(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse(""), "")

    def test_single_character_string(self):
        self.assertEqual(reverse("a"), "a")

    def test_palindrome_string(self):
        self.assertEqual(reverse("radar"), "radar")

    def test_non_palindrome_string(self):
        self.assertEqual(reverse("hello"), "olleh")

    def test_non_string(self):
        with self.assertRaises(TypeError):
            reverse(123)

    def test_iterable_non_string(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 3])

if __name__ == "__main__":
    unittest.main()

