import unittest

import ya_api


class TestYaApi(unittest.TestCase):

    def test_success_create_folder(self):
        self.assertEqual(ya_api.create_folder('test'), 201)

    def test_passed_create_folder(self):
        self.assertEqual(ya_api.create_folder('test_passed'), 409)


