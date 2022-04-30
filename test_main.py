"""Tests for the main.py file"""

import unittest

import pysnooper

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

    def test_modify_status_fails(self):
        """Here's the Test's Docstring."""
        self.assertEqual(m.modify_status("fake_status_id",
                                         "fake_user_id",
                                         "fake_status text",
                                         us.UserStatusCollection()
                                         ),
                         False)

    def test_modify_status_success(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # TODO: add assertion here

    def test_delete_status_false(self):
        """
        Tests searching for a status_id in status_collection, and not
        finding any result.
        """
        self.assertEqual(m.delete_status("fake_status_id",
                                         us.UserStatusCollection()
                                         ),
                         False)

    def test_delete_status_results(self):
        """
        Tests searching for a status_id in status_collection, and not
        getting a result.
        """
        self.assertEqual(True, True)  # TODO: add assertion here

    def test_search_status_none(self):
        """
        Tests searching for a status in status_collection, and not
        finding any results.
        """
        self.assertEqual(m.search_status("fake_status_id",
                                         us.UserStatusCollection()
                                         ),
                         None)

    def test_search_status_results(self):
        """
        Tests searching for a status in status_collection, and getting a
        result.
        """
        self.assertEqual(True, True)  # TODO: add assertion here


if __name__ == '__main__':
    unittest.main()
