import unittest
from unittest.mock import patch
import byx



class TestByx(unittest.TestCase):

    @patch('byx.input', return_value='2207 876234')
    def test_get_doc_owner_name(self, input_mock):
        self.assertEqual(byx.get_doc_owner_name(), 'Василий Гупкин')

    @patch('byx.input', side_effect=['234-158-481-1', 'СНИЛС', 'Masha', '2'])
    def test_add_new_doc(self, input_mock):
        self.assertEqual(byx.add_new_doc(), '2')

    @patch('byx.input', return_value='10006')
    def test_delete_doc(self, input_mock):
        self.assertTrue(byx.delete_doc())
