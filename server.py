from flask import Flask, jsonify
from threading import Lock

app = Flask(__name__)
lock = Lock()

COUNT_FILE = "count.txt"

# ---------- INIT ----------
def init_count():
    try:
        with open(COUNT_FILE, "r"):
            pass
    except:
        with open(COUNT_FILE, "w") as f:
            f.write("0")

init_count()

# ---------- HOME ----------
@app.route("/")
def home():
    return "Backend running"

# ---------- GET USAGE ----------
@app.route("/usage", methods=["GET"])
def usage():
    with lock:
        with open(COUNT_FILE, "r") as f:
            count = f.read().strip()

    return jsonify({
        "schemaVersion": 1,
        "label": "App Uses",
        "message": count,
        "color": "green"
    })

# ---------- POST INCREMENT ----------
@app.route("/usage", methods=["POST"])
def increment_usage():
    with lock:
        with open(COUNT_FILE, "r") as f:
            count = int(f.read().strip())

        count += 1

        with open(COUNT_FILE, "w") as f:
            f.write(str(count))

    return jsonify({"status": "updated", "count": count})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
