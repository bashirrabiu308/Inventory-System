import sqlite3

DB_NAME = 'inventory.db'

def connect_db():
    # Create/connect to the SQLite database and return connection.
    conn = sqlite3.connect(DB_NAME)
    return

def create_tables():
    # Create product and sales tables if they don't exist.
    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity >= 0),
            price REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            type TEXT CHECK(type IN ('sale', 'purchase')),
            quantity INTEGER NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    """)

    conn.commit()
    conn.close()