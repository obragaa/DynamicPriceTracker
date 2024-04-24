import unittest
from data.storage import save_data
import os

class TestStorage(unittest.TestCase):
    def test_save_data(self):
        save_data([{'name': 'Test Product', 'price': '$10'}], 'test_data.json')
        self.assertTrue(os.path.exists('test_data.json'))
        os.remove('test_data.json')
