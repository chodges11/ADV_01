'''
test code for the social network project
'''
# pylint: disable=R0201

from unittest import TestCase

import users

import main


class TestUserCollection(TestCase):
    '''
    tests of the UserCollection class
    '''

    def test_init_collection(self):
        '''
        checks that a collection is initialized and empty
        '''
        coll = main.init_user_collection()

        assert isinstance(coll, users.UserCollection)

        assert len(coll.database) == 0
