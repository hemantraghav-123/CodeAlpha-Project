from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from AWS CI/CD Pipeline!",
        "status": "Running",
        "developer": "Hemant",
        "version": "1.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )