from flask import Flask, request
import datetime
import os

app = Flask(__name__)

LOG_FILE = "/logs/access.log"

@app.route("/")
def home():
    log_entry = f"{datetime.datetime.now()} - Access from {request.remote_addr}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
    return "InfraPulse is running!"

if __name__ == "__main__":
    os.makedirs("/logs", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)

