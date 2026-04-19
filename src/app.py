from flask import Flask, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "database.db"

def get_report_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Example: adjust table/column names to your schema
    cursor.execute("""
    SELECT currency, MAX(rate)
    FROM exchange_rates
    GROUP BY currency
    ORDER BY MAX(rate) DESC
    LIMIT 5
    """)
    
    top_rates = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM exchange_rates")
    total_count = cursor.fetchone()[0]

    conn.close()

    return top_rates, total_count


@app.route("/run", methods=["GET"])
def run_pipeline():
    # Step 1: Run your pipeline
    from main import run_pipeline
    run_pipeline()

    # Step 2: Get data from DB
    top_rates, total_count = get_report_data()

    # Step 3: Format report
    report = """
    <h2>📊 Daily Exchange Rate Report</h2>

    <h3>Top 5 Exchange Rates:</h3>
    <ul>
    """

    for currency, rate in top_rates:
        report += f"<li>{currency}: {rate:.2f}</li>"

    report += f"""
    </ul>

    <p><b>Total currencies processed:</b> {total_count}</p>

    <p>✔ Pipeline executed successfully<br>
    ✔ Data stored in database</p>

    """

    return jsonify({"report": report})

   


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)