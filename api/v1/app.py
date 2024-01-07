#!/usr/bin/env python3
"""Creates a Flask web server"""

from flask import Flask, jsonify, make_response
import os
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__) # creates Flask instance
CORS(app, resources={"/api/*": {"origins": "0.0.0.0"}}) # allows CORS
app.register_blueprint(app_views) # registers blueprint

@app.teardown_appcontext # calls after  request
def tear_down(exception):
    """ when the app context is torn down, remove the current SQLAlchemy Session"""
    storage.close()

@app.errorhandler(404) # handles 404 errors
def not_found(error):
    """ returns a JSON-formatted 404 status code response """
    return make_response(jsonify({"error": "Not found"}), 404)

@app.errorhandler(400) # handles 400 errors
def bad_request(error):
    """ returns a JSON-formatted 400 status code response """
    return make_response(jsonify({"error": "Bad request"}), 400)

if __name__ == "__main__":
    if os.getenv("HBNB_API_HOST") and os.getenv("HBNB_API_PORT"):
        app.run(host=os.getenv("HBNB_API_HOST"),
                port=os.getenv("HBNB_API_PORT")),
    else:
        app.run(host="0.0.0.0", port=5000, threaded=True)