from flask import Flask, jsonify
from main import run_pipeline

app = Flask(__name__)

@app.route("/run")
def run():
    try:
        # Run your pipeline
        run_pipeline()

        # Return formatted report
        return jsonify({
            "report": "📊 Daily Data Pipeline Report\n\n"
                      "✔ Pipeline executed successfully\n"
                      "✔ Data stored in database\n\n"
                      "Automated via n8n workflow"
        })
    except Exception as e:
        # Optional: return error for debugging
        return jsonify({
            "report": f"❌ Pipeline failed: {str(e)}"
        }), 500


if __name__ == "__main__":
    print("Starting server on http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)