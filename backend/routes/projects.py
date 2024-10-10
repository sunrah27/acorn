from flask import Blueprint, request, jsonify
from datetime import datetime
from .db import get_projects_collection

projects_bp = Blueprint('projects', __name__)

# Create a new porject
@projects_bp.route('/projects', methods=['POST'])
def create_project():
    projects_collection = get_projects_collection()
    data = request.json
    
    new_project = {
        'name': data.get('name'),
        'short_name': data.get('short_name'),
        'created_by': data.get('created_by'),               # Need's to be updated after User Login has been sorted out
        'created_at': data.get('created_at'),               # Should be the date and time project was created
        'template': data.get('template', None),             # Optional field for project template
    }

    result = projects_collection.projects.insert_one(new_project)
    return jsonify({'success': True, 'project_id': str(result.inserted_id)}), 201

# Get list of all projects
@projects_bp.route('/projects', methods=['GET'])
def get_projects():
    projects_collection = get_projects_collection()
    projects = list(projects_collection.find({}))
    return jsonify(projects), 200


# Find a specific project based on project Id
@projects_bp.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    projects_collection = get_projects_collection()
    project = projects_collection.find_one({"_id": project_id})

    if project:
        return jsonify(project), 200
    return jsonify({'success': False, 'message': 'Project not found'}), 404

# Update a projects details
@projects_bp.route('/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    projects_collection = get_projects_collection()
    data = request.json

    update_data = {
        'name': data.get('name'),
        'short_name': data.get('short_name'),
        'template': data.get('template', None),
        # Add any other fields you want to update
    }

    result = projects_collection.update_one({"_id": project_id}, {"$set": update_data})  # Update project

    if result.modified_count > 0:
        return jsonify({'success': True}), 200
    return jsonify({'success': False, 'message': 'Project not found or no changes made'}), 404

# Delete project
@projects_bp.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    projects_collection = get_projects_collection()  # Get the projects collection
    result = projects_collection.delete_one({"_id": project_id})  # Delete project

    if result.deleted_count > 0:
        return jsonify({'success': True}), 204
    return jsonify({'success': False, 'message': 'Project not found'}), 404