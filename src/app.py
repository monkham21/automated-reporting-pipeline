from flask import Flask, jsonify, render_template
import sqlite3
from pathlib import Path

app = Flask(__name__)

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "database.db"


def get_dashboard_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT currency, MAX(rate)
        FROM exchange_rates
        GROUP BY currency
        ORDER BY MAX(rate) DESC
        LIMIT 10
    """)
    rows = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM exchange_rates")
    total_count = cursor.fetchone()[0]

    conn.close()

    return rows, total_count


@app.route("/dashboard")
def dashboard():
    rows, total_count = get_dashboard_data()
    return render_template("dashboard.html", rows=rows, total=total_count)

@app.route("/run", methods=["GET"])
def run_pipeline_route():
    from main import run_pipeline
    run_pipeline()  # run your pipeline

    rows, total_count = get_dashboard_data()

    report = f"""
    <h2>📊 Daily Exchange Rate Report</h2>

    <p><b>Date:</b> Today</p>

    <h3>💱 Top 5 Strongest Currencies (vs Base)</h3>
    <ul>
    """

    for currency, rate in rows[:5]:
        report += f"<li><b>{currency}</b>: {rate:,.2f}</li>"

    report += f"""
    </ul>

    <p><b>Total currencies tracked:</b> {total_count}</p>

    <hr>

    <p>✅ Pipeline executed successfully<br>
    ✅ Data updated in database</p>

    <p>🔗 <a href="http://localhost:5000/dashboard">View Full Dashboard</a></p>

    <p><i>Automated via n8n</i></p>
    """

    return jsonify({"report": report})

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True)