import unittest
from db import insert_memory, update_memory, delete_memory, get_by_id, get_all, create_table
from app import chat

class TestBot(unittest.TestCase):

    def test_create_table(self):
        """Create table for testing"""
        create_table()
        return None

    def test_insert_memory(self):
        """Test insert_memory function"""
        cases = [
            {"id": 1, "memory": ["testing database"]},
            {"id": 2, "memory": ["Hello World"]}
        ]
        for case in cases:
            insert_memory(case)
            self.assertEqual(get_by_id(case['id'])[0][1], case['memory'])

    def test_update_memory(self):
        """Test update_memory function"""
        cases = [
            {"id": 1, "memory": ["testing SQLite"]},
            {"id": 2, "memory": ["Hello User"]}
        ]
        for case in cases:
            update_memory(case)
            self.assertEqual(get_by_id(case['id'])[0][1], case['memory'])

    def test_delete_memory(self):
        """Test delete_memory function"""
        cases = [1, 2]
        for case in cases:
            delete_memory(case)
            self.assertEqual(get_by_id(case), [])

if __name__ == '__main__':
    unittest.main()