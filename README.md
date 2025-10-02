

# 🗄️ Inventory Management System – Database & Data Persistence

This project is part of a **team-based Inventory Management System**.
My role is the **Database & Data Persistence Lead**, focusing on designing and implementing the storage layer using **SQLite**.

---

## 📌 Responsibilities

* ✅ Design and implement database/storage layer (SQLite preferred, JSON/CSV acceptable).
* ✅ Create schema for:

  * Products (ID, name, quantity, price)
  * Sales and Purchases
* ✅ Write CRUD functions for product data (Add, Update, Delete, Fetch).
* ✅ Ensure stock levels update correctly after transactions.
* ✅ Add validation logic:

  * No negative stock
  * Prevent duplicate IDs
* ✅ Handle data saving/loading with proper error handling.

**Optional Extensions**

* Supplier details & purchase history
* Encryption for sensitive data (if authentication is added)

---

## 🛠️ Tech Stack

* **Language**: Python
* **Database**: SQLite (built-in with Python)
* **Alternative Storage**: JSON / CSV

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/inventory-management.git
cd inventory-management
```

### 2. Set up virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

---

## 📂 Project Structure

```
inventory-management/
│── database/
│   ├── schema.sql        # Database schema
│   ├── db_handler.py     # SQLite CRUD functions
│── data/
│   ├── backup.json       # Example JSON backup
│── main.py               # Entry point
│── requirements.txt
│── README.md
```

---

## 🧪 Example Features

* Add new product with unique ID
* Update stock after purchase/sale
* Prevent negative stock levels
* Fetch product list

---

## 👥 Team Roles

* **Database & Persistence**: (You ✅)
* **Transaction Handling**: Member 2
* **Reporting**: Member 3
* **GUI Development**: Member 4
