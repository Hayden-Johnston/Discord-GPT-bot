import unittest
import db
import app

class TestBot(unittest.TestCase):

    def test_create_memory(self):
        """Test create_memory function"""
        data = {"user_id": 1, "memory": ["test"]}
        db.insert_memory(data)
        self.assertEqual(db.get_by_id(1)['memory'], ["test"])