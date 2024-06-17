from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://admin:admin%40mongoDB@recruitmenteteam.lt2yva1.mongodb.net/')
db = client['DBRecruitment']
collection = db['JobPosting']

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/job', methods=['POST'])
def post_job():
    job_data = request.json
    if not job_data:
        return jsonify({"error": "Invalid input"}), 400

    # Save to MongoDB
    collection.insert_one(job_data)
    return jsonify({"message": "Job posted successfully!"}), 201

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = list(collection.find())
    return json.loads(json_util.dumps(jobs))

if __name__ == '__main__':
    app.run(debug=True)
