import unittest
from password_policy_compliance.compliance_reporter import generate_compliance_report, audit_password_compliance
from password_policy_compliance.policy_compliance import Policy

class TestComplianceReporter(unittest.TestCase):
    def setUp(self):
        self.policy = Policy(
            name="Test",
            min_length=8,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=True,
            require_special=True
        )
        self.passwords = [
            "StrongP@ss1",  # Compliant
            "weakpass",     # Missing uppercase, digit, and special
            "NoSpecial1",   # Missing special
            "sh0rt",        # Too short, missing uppercase and special
            "Alllowercase123!",  # Missing uppercase (not counting first character)
        ]

    def test_generate_compliance_report(self):
        report = generate_compliance_report(self.passwords, self.policy)
        self.assertEqual(report["total_passwords"], 5)
        self.assertEqual(report["compliant_passwords"], 1)
        self.assertEqual(report["non_compliant_passwords"], 4)
        self.assertEqual(report["compliance_rate"], 20.0)
        self.assertIn("Password must contain at least one uppercase letter (not counting the first character)", report["error_counts"])
        self.assertIn("Password must contain at least one special character", report["error_counts"])
        self.assertIn("Password must be at least 8 characters long", report["error_counts"])

    def test_audit_password_compliance(self):
        audit_results = audit_password_compliance(self.passwords, self.policy)
        self.assertEqual(len(audit_results), 5)
        self.assertTrue(audit_results[0]["compliant"])
        self.assertFalse(audit_results[1]["compliant"])
        self.assertIn("Password must contain at least one special character", audit_results[2]["errors"])
        self.assertIn("Password must be at least 8 characters long", audit_results[3]["errors"])
        self.assertFalse(audit_results[4]["compliant"])
        self.assertIn("Password must contain at least one uppercase letter (not counting the first character)", audit_results[4]["errors"])

if __name__ == '__main__':
    unittest.main()
