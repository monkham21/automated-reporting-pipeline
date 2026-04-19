from pathlib import Path
import sqlite3
from config import DB_PATH

def save_to_db(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    conn = sqlite3.connect(DB_PATH)
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