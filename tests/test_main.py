import unittest
from main import create_connection, fetch_users

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Connect to the existing database file created during the build stage."""
        self.conn = create_connection('week5_project.db')

    def test_fetch_users(self):
        """Test fetching users."""
        users = fetch_users(self.conn)
        self.assertTrue(len(users) > 0)

    def tearDown(self):
        """Close the database connection after each test."""
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
