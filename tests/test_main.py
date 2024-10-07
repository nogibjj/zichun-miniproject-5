import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import create_connection, insert_user, fetch_users

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Set up an in-memory database before each test."""
        self.conn = create_connection(":memory:")  # Use an in-memory database
        self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                age INTEGER);''')

    def test_insert_user(self):
        """Test inserting a new user."""
        insert_user(self.conn, 'TestUser', 22)
        users = fetch_users(self.conn)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], 'TestUser')

    def tearDown(self):
        """Close the database connection after each test."""
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
