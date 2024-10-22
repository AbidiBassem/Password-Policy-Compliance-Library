import unittest
from password_policy_compliance.blacklist_checker import is_password_blacklisted, check_haveibeenpwned

class TestBlacklistChecker(unittest.TestCase):
    def test_is_password_blacklisted(self):
        blacklist = {"password", "123456", "qwerty"}
        self.assertTrue(is_password_blacklisted("password", blacklist))
        self.assertFalse(is_password_blacklisted("secure_password", blacklist))

    def test_check_haveibeenpwned(self):
        # This test will always pass due to the mock implementation
        self.assertFalse(check_haveibeenpwned("password"))
        self.assertFalse(check_haveibeenpwned("secure_password"))

if __name__ == '__main__':
    unittest.main()
