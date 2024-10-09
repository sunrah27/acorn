from flask import Flask
from flask_cors import CORS
from api import api_bp  # Import the API blueprint

app = Flask(__name__)
CORS(app)

# Register the API blueprint
app.register_blueprint(api_bp)

@app.route('/')
def home():
    return "Welcome to Acorn API!"

if __name__ == '__main__':
    app.run(debug=True)