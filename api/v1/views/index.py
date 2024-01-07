#!/usr/bin/env python3
""" index.py endpoint that retrieves the number of each objects """

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage



@app_views.route('/states')
def status_ok():
    """ returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})

@app_views.route('/stats')
def get_stats():
    """ retrieves the number of each objects by type """
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
