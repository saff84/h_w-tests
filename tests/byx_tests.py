import unittest
from unittest.mock import patch
import byx



class TestByx(unittest.TestCase):

    @patch('byx.input', return_value='2207 876234')
    def test_get_doc_owner_name(self, input_mock):
        '''По номеру документа получаем ФИО'''
        self.assertEqual(byx.get_doc_owner_name(), 'Василий Гупкин')

    @patch('byx.input', side_effect=['234-158-481-1', 'СНИЛС', 'Masha', '2'])
    def test_add_new_doc(self, input_mock):
        '''Создание нового документа успешно'''
        self.assertEqual(byx.add_new_doc(), '2')

    @patch('byx.input', return_value='10006')
    def test_delete_doc(self, input_mock):
        '''Удаление документа успешно'''
        self.assertTrue(byx.delete_doc())

    @patch('byx.input', return_value='4')
    def test_add_new_shelf(self, input_mock):
        '''Создание новой полки успешно'''
        self.assertTrue(byx.add_new_shelf())

    def test_get_all_doc_owners_names(self):
        '''Вывод всех ФИО успешно'''
        self.assertTrue(byx.get_all_doc_owners_names())