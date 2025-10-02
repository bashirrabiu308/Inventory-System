📦 Inventory Management System (GUI)

An Inventory Management System built with Python, designed to help track products, manage sales/purchases, and generate reports. The system uses SQLite for reliable data persistence and includes a GUI for user-friendly interaction.

🚀 Features

Product Management (CRUD)

Add, update, delete, and fetch products

Prevent negative stock and duplicate entries

Database & Persistence

SQLite database for data storage

Safe error handling (connection, integrity, validation)

Transactions

Record sales and purchases

Ensure stock updates correctly

Reporting & Analytics

Generate inventory and sales reports

Export to CSV or PDF

Visualize data with charts

Graphical User Interface (GUI)

Simple and intuitive navigation

Forms for adding/updating products

Views for reports and stock levels

🏗 Project Structure
InventorySystem/
│
├── database.py        # Database & persistence layer (SQLite)
├── transactions.py    # Business logic for sales/purchases
├── reports.py         # Reporting & analytics
├── gui.py             # Graphical User Interface (Tkinter/PyQt/Kivy)
├── main.py            # Entry point of the application
└── README.md          # Project documentation

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/your-username/inventory-system.git
cd inventory-system


Set up a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies

pip install -r requirements.txt


(Note: SQLite comes pre-installed with Python, so no extra setup is required.)

▶️ Usage

Run the application:

python main.py


Sample test (from main.py):

from database import create_tables, add_product, get_products

create_tables()
add_product(1, "Laptop", 10, 350000)
print(get_products())

👥 Team Roles

@Allamah 3 – Database & Data Persistence Lead

Designed database schema (products, transactions)

Implemented CRUD functions with validation & error handling

@Muhammad Imam Umar – Core Logic & Transactions Developer

Handles sales/purchases logic

Implements stock rules and alerts

@bashirrabiu308 – Reporting & Analytics Developer

Generates reports and charts

Exports data to CSV/PDF

@Dandina53 – GUI & User Experience Developer

Builds graphical user interface

Integrates modules into a user-friendly system

📌 Contribution Workflow

Create a new branch for your task:

git checkout -b feature-branch-name


Commit your changes with clear messages:

git commit -m "Added CRUD functions for database"


Push your branch:

git push origin feature-branch-name


Open a Pull Request for review.

📷 Screenshots (To Be Added)

Product management view

Sales report example

Inventory dashboard

📝 Future Improvements

Authentication (admin vs cashier roles)

Supplier management & purchase history

Encryption for sensitive data

Trend forecasting with statistics

📄 License

This project is licensed under the MIT License – you are free to use, modify, and distribute with attribution.
