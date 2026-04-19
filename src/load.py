from pathlib import Path
import sqlite3

def save_to_db(data):
    BASE_DIR = Path(__file__).resolve().parent.parent
    db_path = BASE_DIR / "data" / "database.db"

    conn = sqlite3.connect(db_path)
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