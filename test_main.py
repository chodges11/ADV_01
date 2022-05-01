"""Tests for the main.py file"""

# pylint: disable = import-error

import unittest
from mock import Mock, patch
# TODO: REMOVE
import pysnooper

import main as m
import users as u
import user_status as us

# pylint: disable=R0904


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

    def test_save_status_updates_fails(self):
        """Here's the Test's Docstring."""
        self.assertEqual(m.save_status_updates("fake_file",
                                               us.UserStatusCollection()),
                         False) # TODO: add assertion here

    def test_save_status_updates_success(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # TODO: add assertion here

    def test_add_user_fails(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # TODO: add assertion here

    def test_add_user_success(self):
        """Here's the Test's Docstring."""
        self.assertEqual(m.add_user("fake_user_id",
                                    "fake_email",
                                    "fake_user_name",
                                    "fake_user_last_name",
                                    u.UserCollection()
                                    ),
                         True)

    def test_modify_user_fails(self):
        """Here's the Test's Docstring."""
        self.assertEqual(m.modify_user("fake_user_id",
                                       "fake_email",
                                       "fake_user_name",
                                       "fake_user_last_name",
                                       u.UserCollection()
                                       ),
                         False)

    def test_modify_user_success(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # TODO: add assertion here

    def test_delete_user_fails(self):
        """Here's the Test's Docstring."""
        self.assertEqual(m.delete_user("fake_user_id", u.UserCollection()),
                         False)

    def test_delete_user_success(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # TODO: add assertion here

    def test_search_user_none(self):
        """Here's the Test's Docstring."""
        self.assertEqual(m.search_user("fake_user_id", u.UserCollection()),
                         None)

    def test_search_user_results(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # TODO: add assertion here

    def test_add_status_fails(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # TODO: add assertion here

    def test_add_status_success(self):
        """Here's the Test's Docstring."""
        self.assertEqual(True, True)  # TODO: add assertion here

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
        self.assertEqual(False, m.delete_status("fake_status_id",
                                         us.UserStatusCollection()
                                         )
                         )

    def test_delete_status_results(self):
        """
        Tests searching for a status_id in status_collection, and not
        getting a result.
        """
        tmp_user_status = us.UserStatus('fake_status_id',
                                        'fake_user_id',
                                        'fake_status_text')
        tmp_user_status_collection = us.UserStatusCollection()
        tmp_user_status_collection.add_status(
            tmp_user_status.status_id,
            tmp_user_status.user_id,
            tmp_user_status.status_text
        )

        self.assertEqual(True,
                         m.delete_status('fake_status_id',
                                         tmp_user_status_collection
                                         )
                         )

    def test_search_status_none(self):
        """
        Tests searching for a status in status_collection, and not
        finding any results.
        """
        self.assertEqual(None, m.search_status("fake_status_id",
                                               us.UserStatusCollection()
                                               )
                         )

    def test_search_status_results(self):
        """
        Tests searching for a status in status_collection, and getting a
        result.
        """
        tmp_user_status = us.UserStatus('fake_status_id',
                                        'fake_user_id',
                                        'fake_status_text')
        tmp_user_status_collection = us.UserStatusCollection()
        tmp_user_status_collection.add_status(
            tmp_user_status.status_id,
            tmp_user_status.user_id,
            tmp_user_status.status_text
        )

        self.assertEqual(tmp_user_status_collection,
                         m.search_status('fake_status_id',
                                         tmp_user_status_collection
                                         )
                         )


if __name__ == '__main__':
    unittest.main()
