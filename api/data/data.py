from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://latmongo:mongolat@mongocluster.4akrr.mongodb.net/?retryWrites=true&w=majority&appName=mongoCluster")
db = client['testLat']
collection = db['dataMongo']

@app.route('/data', methods=['GET'])
def get_data():  
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)  