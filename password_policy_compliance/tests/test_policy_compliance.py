import unittest
from password_policy_compliance.policy_compliance import get_policy, create_custom_policy, Policy

class TestPolicyCompliance(unittest.TestCase):
    def test_get_nist_policy(self):
        policy = get_policy("NIST")
        self.assertEqual(policy.name, "NIST")
        self.assertEqual(policy.min_length, 8)
        self.assertFalse(policy.require_uppercase)
        self.assertFalse(policy.require_lowercase)
        self.assertFalse(policy.require_digits)
        self.assertFalse(policy.require_special)

    def test_get_owasp_policy(self):
        policy = get_policy("OWASP")
        self.assertEqual(policy.name, "OWASP")
        self.assertEqual(policy.min_length, 10)
        self.assertTrue(policy.require_uppercase)
        self.assertTrue(policy.require_lowercase)
        self.assertTrue(policy.require_digits)
        self.assertTrue(policy.require_special)

    def test_get_unknown_policy(self):
        with self.assertRaises(ValueError):
            get_policy("UNKNOWN")

    def test_create_custom_policy(self):
        custom_policy = create_custom_policy(
            name="Custom",
            min_length=12,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=False,
            require_special=True
        )
        self.assertEqual(custom_policy.name, "Custom")
        self.assertEqual(custom_policy.min_length, 12)
        self.assertTrue(custom_policy.require_uppercase)
        self.assertTrue(custom_policy.require_lowercase)
        self.assertFalse(custom_policy.require_digits)
        self.assertTrue(custom_policy.require_special)

if __name__ == '__main__':
    unittest.main()
