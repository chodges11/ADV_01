"""Tests for the main.py file"""

import unittest
import main as m
import users as u
import user_status as us


class MainTestCase(unittest.TestCase):
    """Here's the Class Docstring."""

    def test_init_user_collection(self):
        """Here's the Test's Docstring. Since they are both located at
        different memory locations, I verified the type was the same.
        """
        new_user_collection = u.UserCollection()
        self.assertEqual(type(m.init_user_collection()),
                         type(new_user_collection))

    def test_init_status_collection(self):
        """Here's the Test's Docstring. Since they are both located at
        different memory locations, I verified the type was the same.
        """
        new_status_collection = us.UserStatusCollection()
        self.assertEqual(type(m.init_status_collection()),
                         type(new_status_collection))

    def test_load_users(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_save_users(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_load_status_updates(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_save_status_updates(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_add_user(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_modify_user(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_delete_user(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_search_user(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_add_status(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_modify_status(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_delete_status(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here

    def test_search_status(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
