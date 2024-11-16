import unittest
from utils.file_handler import save_data, load_data

class TestFileHandler(unittest.TestCase):
    def test_save_load_data(self):
        data = {"transactions": ["Groceries - 100"], "budget": "500"}
        save_data(data)
        loaded_data = load_data()
        self.assertEqual(loaded_data, data)

if __name__ == "__main__":
    unittest.main()
