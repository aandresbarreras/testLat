from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import ConnectionError

app = Flask(__name__)

mongo_uri = os.getenv('MONGODB_URI')

try:
    client = MongoClient(mongo_uri)
    db = client['testLat']
    collection = db['dataMongo']
    print(f"Conectado a la base de datos.")
except ConnectionError as e:
    print("Error al conectar a la base de datos:", e)

@app.route('/data', methods=['GET'])
def get_data():
    try:
        data = list(collection.find({}, {'_id': 0}))
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
