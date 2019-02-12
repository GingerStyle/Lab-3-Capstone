import unittest
from unittest import TestCase
import Part1CamelCase

class TestCamelCase(TestCase):

    def test_split_sentence(self):
        list_of_words = Part1CamelCase.split_sentence('all of these words')
        self.assertIn({'all', 'of', 'these', 'words'}, list_of_words)

    def test_process_sentence(self):
        list_of_words = Part1CamelCase.process_sentence({'all', 'of', 'these', 'words'})
        self.assertEqual({'all', 'Of', 'These', 'Words'}, list_of_words)


#if __name__ == '__main__':
#    unittest.main()