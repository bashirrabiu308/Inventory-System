import sqlite3

DB_NAME = "inventory.db"


def connect_db():
    """Create/connect to the SQLite database safely."""
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None


def create_tables():
    """Create product and transactions tables if they don’t exist."""
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()

    try:
        # Create products table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity >= 0),
                price REAL NOT NULL CHECK(price >= 0)
            )
        """)

        # Create transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                type TEXT CHECK(type IN ('sale', 'purchase')),
                quantity INTEGER NOT NULL CHECK(quantity > 0),
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(product_id) REFERENCES products(id)
            )
        """)

        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)
    finally:
        conn.close()


# ---------------- CRUD Functions ---------------- #

def add_product(product_id, name, quantity, price):
    """Add a new product with validation checks."""
    if quantity < 0:
        print("Error: Quantity cannot be negative.")
        return
    if price < 0:
        print("Error: Price cannot be negative.")
        return

    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
                       (product_id, name, quantity, price))
        conn.commit()
        print(f"Product '{name}' added successfully.")
    except sqlite3.IntegrityError as e:
        print("Integrity Error:", e)  # Handles duplicate IDs/names
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def get_products():
    """Fetch all products from the database."""
    conn = connect_db()
    if conn is None:
        return []

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print("Error fetching products:", e)
        return []
    finally:
        conn.close()


def update_product(product_id, quantity=None, price=None):
    """Update product quantity or price with validation."""
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT quantity, price FROM products WHERE id=?", (product_id,))
        row = cursor.fetchone()
        if not row:
            print("Error: Product not found.")
            return

        # Validate quantity update
        if quantity is not None:
            if quantity < 0:
                print("Error: Quantity cannot be negative.")
                return
            cursor.execute("UPDATE products SET quantity=? WHERE id=?", (quantity, product_id))

        # Validate price update
        if price is not None:
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            cursor.execute("UPDATE products SET price=? WHERE id=?", (price, product_id))

        conn.commit()
        print(f"Product ID {product_id} updated successfully.")
    except sqlite3.Error as e:
        print("Error updating product:", e)
    finally:
        conn.close()


def delete_product(product_id):
    """Delete a product by ID."""
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        conn.commit()
        print(f"Product ID {product_id} deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting product:", e)
    finally:
        conn.close()
