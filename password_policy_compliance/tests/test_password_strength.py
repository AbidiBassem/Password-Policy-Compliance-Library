import unittest
from password_policy_compliance.password_strength import calculate_entropy, score_password

class TestPasswordStrength(unittest.TestCase):
    def test_calculate_entropy(self):
        self.assertAlmostEqual(calculate_entropy("password"), 37.604, places=3)
        self.assertAlmostEqual(calculate_entropy("P@ssw0rd"), 52.437, places=3)
        self.assertEqual(calculate_entropy(""), 0)

    def test_score_password(self):
        weak_score = score_password("password")
        medium_score = score_password("P@ssw0rd")
        strong_score = score_password("MyC0mpl3xP@ssw0rd!")

        self.assertLess(weak_score["score"], medium_score["score"])
        self.assertLessEqual(medium_score["score"], strong_score["score"])

        self.assertEqual(weak_score["length"], 32)
        self.assertEqual(weak_score["uppercase"], 0)
        self.assertEqual(weak_score["lowercase"], 10)
        self.assertEqual(weak_score["digits"], 0)
        self.assertEqual(weak_score["special"], 0)

        self.assertEqual(medium_score["uppercase"], 10)
        self.assertEqual(medium_score["lowercase"], 10)
        self.assertEqual(medium_score["digits"], 10)
        self.assertEqual(medium_score["special"], 10)

        self.assertGreater(strong_score["entropy"], medium_score["entropy"])

    def test_score_password_patterns(self):
        repeated_chars = score_password("aaabbbccc")
        sequential_letters = score_password("abcdefgh")
        sequential_numbers = score_password("12345678")

        self.assertLessEqual(repeated_chars["score"], 52)
        self.assertLessEqual(sequential_letters["score"], 52)
        self.assertLessEqual(sequential_numbers["score"], 52)

if __name__ == '__main__':
    unittest.main()
