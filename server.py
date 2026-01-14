from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend running"

@app.route("/usage")
def usage():
    with open("count.txt") as f:
        count = f.read().strip()

    return jsonify({
        "schemaVersion": 1,
        "label": "App Uses",
        "message": count,
        "color": "green"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
