#!/usr/bin/python3
"""
Index html link
"""


from api.v1.views import app_views
from flask import Flask, jsonify

# routes


@app_views.route('/status', methods=['GET'])
def status():
    """Teyire working"""
    return jsonify({"status": "Ok"})
