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

def add_product(product_id, name, quantity, price):
    """Add a new product."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
                       (product_id, name, quantity, price))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print("Error:", e)  # Handle duplicate IDs/names
    conn.close()

def get_products():
    """Fetch all products."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_product(product_id, quantity=None, price=None):
    """Update product quantity or price."""
    conn = connect_db()
    cursor = conn.cursor()
    if quantity is not None:
        cursor.execute("UPDATE products SET quantity=? WHERE id=?", (quantity, product_id))
    if price is not None:
        cursor.execute("UPDATE products SET price=? WHERE id=?", (price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    """Delete a product by ID."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
