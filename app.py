from flask import Flask, jsonify
import socket
import os
import datetime
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "🚀 Flask App Running Successfully!",
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "environment": os.getenv("ENV", "Development"),
        "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": platform.python_version()
    }

@app.route("/health")
def health():
    return jsonify(status="UP", message="Application is healthy ✅")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
