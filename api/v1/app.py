#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

# creating an  instance of Flask
app = Flask(__name__)

# blue print app_views
app.register_blueprint(app_views)

# configure flask to Nice Json
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Enable CORS fo all routes, allowing access from any origin
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(error):
    """
    Clean-up method
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    Custom 404 error
    """
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    """Running condition
    """
    app.run(host=getenv('HBNB_API_HOST'),
            port=getenv('HBNB_API_PORT'),
            threaded=True)
