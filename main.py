from data_base import create_tables, add_product, get_products, update_product, delete_product

# Create tables
create_tables()

# Add products
add_product(1, "Laptop", 10, 350000)
add_product(2, "Phone", 5, 150000)
add_product(1, "Tablet", 7, 120000)  # Duplicate ID, will raise error

# Show products
print("Current Products:", get_products())

# Update product
update_product(1, quantity=8, price=360000)
update_product(2, quantity=-5)  # Negative quantity, will raise error

# Delete product
delete_product(2)

# Show final products
print("Final Products:", get_products())
