import unittest
from password_policy_compliance.password_generator import generate_password, generate_passphrase
from password_policy_compliance.policy_compliance import Policy

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.policy = Policy(
            name="Test",
            min_length=8,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=True,
            require_special=True
        )

    def test_generate_password(self):
        password = generate_password(12, self.policy)
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(not c.isalnum() for c in password))

    def test_generate_password_min_length(self):
        with self.assertRaises(ValueError):
            generate_password(7, self.policy)

    def test_generate_passphrase(self):
        word_list = ["apple", "banana", "cherry", "date", "elderberry"]
        passphrase = generate_passphrase(4, word_list)
        self.assertEqual(len(passphrase.split("-")), 4)
        for word in passphrase.split("-"):
            self.assertIn(word, word_list)

    def test_generate_passphrase_min_words(self):
        word_list = ["apple", "banana", "cherry"]
        with self.assertRaises(ValueError):
            generate_passphrase(2, word_list)

if __name__ == '__main__':
    unittest.main()
