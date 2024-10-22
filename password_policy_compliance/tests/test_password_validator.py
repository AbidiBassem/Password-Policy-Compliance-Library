import unittest
from password_policy_compliance.password_validator import validate_password
from password_policy_compliance.policy_compliance import Policy

class TestPasswordValidator(unittest.TestCase):
    def setUp(self):
        self.policy = Policy(
            name="Test",
            min_length=8,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=True,
            require_special=True
        )

    def test_valid_password(self):
        result = validate_password("StrongP@ss1", self.policy)
        self.assertTrue(result["valid"])
        self.assertEqual(len(result["errors"]), 0)

    def test_short_password(self):
        result = validate_password("Sh0rt!", self.policy)
        self.assertFalse(result["valid"])
        self.assertIn("Password must be at least 8 characters long", result["errors"])

    def test_missing_uppercase(self):
        result = validate_password("p@ssw0rd", self.policy)
        self.assertFalse(result["valid"])
        self.assertIn("Password must contain at least one uppercase letter", result["errors"])

    def test_missing_lowercase(self):
        result = validate_password("P@SSW0RD", self.policy)
        self.assertFalse(result["valid"])
        self.assertIn("Password must contain at least one lowercase letter", result["errors"])

    def test_missing_digit(self):
        result = validate_password("P@ssword", self.policy)
        self.assertFalse(result["valid"])
        self.assertIn("Password must contain at least one digit", result["errors"])

    def test_missing_special(self):
        result = validate_password("Passw0rd", self.policy)
        self.assertFalse(result["valid"])
        self.assertIn("Password must contain at least one special character", result["errors"])

    def test_multiple_errors(self):
        result = validate_password("pass", self.policy)
        self.assertFalse(result["valid"])
        self.assertEqual(len(result["errors"]), 4)

    def test_all_lowercase_with_digit_and_special(self):
        result = validate_password("alllowercase123!", self.policy)
        self.assertFalse(result["valid"])
        self.assertIn("Password must contain at least one uppercase letter", result["errors"])

    def test_first_letter_uppercase_rest_lowercase(self):
        result = validate_password("Alllowercase123!", self.policy)
        self.assertFalse(result["valid"])
        self.assertIn("Password must contain at least one uppercase letter (not counting the first character)", result["errors"])

if __name__ == '__main__':
    unittest.main()
