import unittest
from auth_service import register_user
class TestAuth(unittest.TestCase):
    def test_register_user(self):
        users = {}
        result = register_user("abdullah", "pass123", users)
        self.assertEqual(result["username"], "abdullah")
        self.assertTrue(result["registered"])
        self.assertNotEqual(users["abdullah"], "pass123")
    def test_duplicate_username(self):
        users = {}
        register_user("abdullah", "pass123", users)
        with self.assertRaises(ValueError):
            register_user("abdullah", "anotherpass", users)
    def test_empty_username(self):
        with self.assertRaises(ValueError):
            register_user("", "pass123", {})
    def test_empty_password(self):
        with self.assertRaises(ValueError):
            register_user("abdullah", "", {})
if __name__ == "__main__":
    unittest.main()
