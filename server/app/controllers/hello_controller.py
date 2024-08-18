from flask import Blueprint, jsonify

hello_blueprint = Blueprint('hello', __name__)

@hello_blueprint.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})