# main.py
import sqlite3

def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    """Create a table."""
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            age INTEGER);''')

def insert_user(conn, name, age):
    """Insert a new user into the table."""
    with conn:
        conn.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))

def fetch_users(conn):
    """Fetch all users."""
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    return cur.fetchall()

if __name__ == '__main__':
    # Create or connect to a persistent database file
    database = "week5_project.db"
    conn = create_connection(database)
    
    # Perform the necessary CRUD operations
    create_table(conn)
    insert_user(conn, 'Alice', 30)
    insert_user(conn, 'Bob', 25)

    # Fetch and print users
    users = fetch_users(conn)
    print("Users:", users)
    
    conn.close()
