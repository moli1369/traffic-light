from flask import Flask, request, jsonify

app = Flask(__name__)

# وضعیت اولیه چراغ راهنمایی (مقدار پیش‌فرض)
# Ausgangszustand der Ampel (Standardwert)
traffic_light_status = "RED"

# روت برای دریافت وضعیت فعلی چراغ راهنمایی
# Rooten Sie, um den aktuellen Ampelstatus abzurufen
@app.route('/status', methods=['GET'])
def get_traffic_light_status():
    return jsonify({"status": traffic_light_status})

# روت برای تنظیم وضعیت چراغ راهنمایی
# Rooten Sie, um den Ampelstatus einzustellen
@app.route('/set_status', methods=['POST'])
def set_traffic_light_status():
    global traffic_light_status
    new_status = request.json.get('status')
    if new_status in ["RED", "GREEN"]:
        traffic_light_status = new_status
        return jsonify({"message": "Traffic light status updated successfully."})
    else:
        return jsonify({"error": "Invalid status provided."}), 400

if __name__ == '__main__':
    app.run(debug=True)
