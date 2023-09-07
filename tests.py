import unittest
from db import insert_memory, update_memory, delete_memory, get_by_id, get_all, create_table
from app import handle_memory

class TestBot(unittest.TestCase):

    def test_a_create_table(self):
        """Create table for testing"""
        create_table()
        return None

    def test_b_insert_memory(self):
        """Test insert_memory function"""
        cases = [
            {"id":1, "memory": "testing database"},
            {"id":2, "memory": "Hello World"}
        ]
        for case in cases:
            insert_memory(case)
            self.assertEqual(get_by_id(case['id'])[0][1], case['memory'])

    def test_c_update_memory(self):
        """Test update_memory function"""
        cases = [
            {"id":1, "memory": "testing SQLite"},
            {"id":2, "memory": "Hello User"}
        ]
        for case in cases:
            update_memory(case)
            self.assertEqual(get_by_id(case['id'])[0][1], case['memory'])

    def test_d_delete_memory(self):
        """Test delete_memory function"""
        cases = [1, 2]
        for case in cases:
            delete_memory(case)
            self.assertEqual(get_by_id(case), [])

    def test_e_handle_memory(self):
        """Test handle_memory function"""
        cases = [
            {"id":1, "prompt": "testing database"},
            {"id":1, "prompt": "Hello database"},
            {"id":1, "prompt": "Hello everyone"},
            {"id":1, "prompt": "Hello world"},
        ]
        for case in cases:
            handle_memory(case['id'], case['prompt'])
        self.assertEqual(get_by_id(1)[0][1].split(", "), ["Hello everyone", "Hello world"])
        delete_memory(1)

if __name__ == '__main__':
    unittest.main()