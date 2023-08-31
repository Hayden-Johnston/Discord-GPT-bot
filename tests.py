import unittest
from db import insert_memory, update_memory, delete_memory, get_by_id, get_all, create_table
import app

class TestBot(unittest.TestCase):

    def test_create_table(self):
        """Create table for testing"""
        create_table()
        return None

    def test_insert_memory(self):
        """Test insert_memory function"""
        cases = [
            {"user_id": 1, "memory": ["testing database"]},
            {"user_id": 2, "memory": ["hello world"]}
        ]
        for case in cases:
            insert_memory(case)
            row = get_by_id(case['user_id'])
            self.assertEqual(get_by_id(case['user_id'])['memory'], case['memory'])

    def test_update_memory(self):
        """Test update_memory function"""
        cases = [
            {"user_id": 1, "memory": ["testing SQLite"]},
            {"user_id": 2, "memory": ["hello discord"]}
        ]
        for case in cases:
            update_memory(case)
            self.assertEqual(get_by_id(case['user_id'])['memory'], case['memory'])

    def delete_memory(self):
        """Test delete_memory function"""
        cases = [ 1, 2]
        for case in cases:
            delete_memory(case)
            self.assertEqual(get_by_id(case), None)

if __name__ == '__main__':
    unittest.main()