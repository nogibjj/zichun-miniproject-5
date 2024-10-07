import sqlite3

def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    """Create the users table if it doesn't exist."""
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            age INTEGER);''')

def insert_user(conn, name, age):
    """Insert a new user into the users table."""
    with conn:
        conn.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))

def update_user(conn, user_id, name, age):
    """Update a user's name and age by their ID."""
    with conn:
        conn.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))

def delete_user(conn, user_id):
    """Delete a user by their ID."""
    with conn:
        conn.execute('DELETE FROM users WHERE id = ?', (user_id,))

def fetch_users(conn):
    """Fetch and return all users."""
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    return cur.fetchall()

if __name__ == '__main__':
    # Connect to database
    database = "week5_project.db"
    conn = create_connection(database)
    
    # Create table
    create_table(conn)
    
    # Insert users
    insert_user(conn, 'Alice', 30)
    insert_user(conn, 'Bob', 25)
    
    # Read users (before update)
    print("Users (before update):", fetch_users(conn))
    
    # Update user
    update_user(conn, 1, 'Alice Smith', 31)
    
    # Read users (after update)
    print("Users (after update):", fetch_users(conn))
    
    # Delete user
    delete_user(conn, 2)
    
    # Read users (after delete)
    print("Users (after delete):", fetch_users(conn))
    
    conn.close()
