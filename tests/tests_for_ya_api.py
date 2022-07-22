import unittest

import ya_api


class TestYaApi(unittest.TestCase):

    def test_success_create_folder(self):
        '''Создание успешно'''
        self.assertEqual(ya_api.create_folder('test'), 201)

    def test_success_create_folder(self):
        '''Папка уже существует'''
        self.assertEqual(ya_api.create_folder('test'), 409)

    def test_success_create_folder(self):
        '''Не авторизован'''
        self.assertEqual(ya_api.create_folder('test'), 401)

    def test_passed_create_folder(self):
        '''Удаление успешно'''
        self.assertEqual(ya_api.delete_folder('test'), 204)


