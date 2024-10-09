from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.acorn

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    project = {
        "name": data['name'],
        "short_name": data['short_name'],
        "created_by": data['created_by'],
        "created_at": datetime.now(),
    }
    result = db.projects.insert_one(project)
    return jsonify({"id": str(result.inserted_id), "message": "Project created successfully"}), 201

@projects_bp.route('/projects', methods=['GET'])
def get_projects():
    projects = list(db.projects.find({}))
    for project in projects:
        project['_id'] = str(project['_id'])  # Convert ObjectId to string
    return jsonify(projects), 200
