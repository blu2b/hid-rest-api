from flask import Flask, request, jsonify
from hid_writer import type_text
import time

app = Flask(__name__)

@app.route("/type", methods=["POST"])
def type_body():
    data = request.get_json(silent=True) or {}
    if "text" not in data:
        return jsonify({"status": "error", "error": "Missing 'text' in JSON body"}), 400
    text = data["text"]

    layout = "DE" # default german
    if "keyboard_layout" in data:
        layout = data["keyboard_layout"].upper()
    type_text(text, layout)
    return {"status": "ok", "typed": text, "keyboard layout": layout}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
