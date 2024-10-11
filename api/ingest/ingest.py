from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = os.getenv('MONGODB_URI')

client = MongoClient(mongo_uri)
db = client['testLat']
collection = db['dataMongo']

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json
    if data is None:
        return jsonify({"error": "No JSON data provided."}), 400

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid data format. Expected a JSON object."}), 400

    collection.insert_one(data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
