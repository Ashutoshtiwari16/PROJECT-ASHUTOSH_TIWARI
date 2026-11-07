import sqlite3

# Name of our database file
DATABASE_NAME = "data/expenses.db"


def create_table():
    """Create the expenses table if it doesn't already exist."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def add_expense(amount, category, description):
    """Add a new expense to the database."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, description)
        VALUES (?, ?, ?)
    """, (amount, category, description))

    connection.commit()
    connection.close()


def get_total_expenses():
    """Get the total amount of all expenses."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    result = cursor.fetchone()[0]

    connection.close()

    return result if result is not None else 0