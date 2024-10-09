from flask import Blueprint

# Create a blueprint for the API
api_bp = Blueprint('api', __name__)

# Import the projects routes
from .projects import projects_bp

# Register the projects blueprint
api_bp.register_blueprint(projects_bp, url_prefix='/api')