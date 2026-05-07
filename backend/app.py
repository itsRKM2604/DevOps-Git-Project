from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URL")

client = MongoClient(MONGO_URI)
db = client.test
collection = db['git-user-flask-db']

app = Flask(__name__)

@app.route("/submittodoitem", methods=['POST'])
def submitToDoItem():
    formdata = dict(request.json)
    collection.insert_one(formdata)

    return jsonify({
        "success": True,
        "message": "Data inserted Successfully"
    }),200

if __name__ == "__main__":
    app.run(port=9001)