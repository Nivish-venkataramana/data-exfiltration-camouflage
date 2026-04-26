from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

from pipeline import process_packet
from detect import detect

app = Flask(__name__)
CORS(app)

# Store logs
logs = []
# Track stolen files (state of vault)
stolen_files = set()


@app.route('/event', methods=['POST'])
def event():

    data = request.json
    file = data.get("file")

    # 🚫 Prevent duplicate attacks on same file
    if file in stolen_files:
        return jsonify({
            "message": "File already exfiltrated",
            "file": file
        })

    # 🔍 Feature extraction + ML detection
    features = process_packet(file)
    result = detect(features)

    # 🧠 Create log entry
    entry = {
        "file": file,
        "result": result["label"],   # ALERT / NORMAL
        "score": result["score"],
        "time": datetime.now().strftime("%H:%M:%S"),
        "status": "EXFILTRATED"
    }

    # Save state
    logs.append(entry)
    stolen_files.add(file)

    return jsonify(entry)


@app.route('/logs', methods=['GET'])
def logs_api():
    return jsonify(logs)


@app.route('/vault', methods=['GET'])
def vault_state():
    """
    Returns current vault state
    Useful if you want frontend to know which files are gone
    """
    return jsonify({
        "stolen_files": list(stolen_files)
    })


if __name__ == "__main__":
    app.run(debug=True)