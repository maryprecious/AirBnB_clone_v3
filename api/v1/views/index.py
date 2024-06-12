#!/usr/bin/python3
"""
Index html link
"""

from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify

# routes


@app_views.route('/status', methods=['GET'])
def status():
    """Get Status"""
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats', methods=['GET'])
def stats():
    """Gettings stats"""
    return jsonify({storage.count(): 'age'})
