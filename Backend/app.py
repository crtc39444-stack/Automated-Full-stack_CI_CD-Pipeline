from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

FRONTEND_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Frontend")
)


@app.route("/")
def home():
    return send_from_directory(FRONTEND_FOLDER, "index.html")


@app.route("/style.css")
def style():
    return send_from_directory(FRONTEND_FOLDER, "style.css")


@app.route("/script.js")
def script():
    return send_from_directory(FRONTEND_FOLDER, "script.js")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)