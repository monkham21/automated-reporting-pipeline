import sqlite3

def save_to_db(data):
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            currency TEXT,
            rate REAL
        )
    """)

    for row in data:
        cursor.execute(
            "INSERT INTO exchange_rates VALUES (?, ?)",
            (row["currency"], row["rate"])
        )

    conn.commit()
    conn.close()