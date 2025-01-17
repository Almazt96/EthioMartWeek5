def test_store():
    assert 1 + 1 == 2

import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()
    
import unittest

class TestProcessData(unittest.TestCase):
    def test_clean_data(self):
        raw_data = "sample data"
        self.assertEqual(clean_data(raw_data), "cleaned data")
