"""
    API REST con Python 3 y SQLite 3
"""
from flask import Flask, jsonify, request
import user_controller
from db import create_tables

app = Flask(__name__)


@app.route('/users', methods=["GET"])
def get_users():
    users = user_controller.get_users()
    return jsonify(users)


@app.route("/user", methods=["POST"])
def insert_user():
    user_details = request.get_json()
    name = user_details["name"]
    last_name = user_details["last_name"]
    user_name = user_details["user_name"]
    email = user_details["email"]
    result = user_controller.insert_user(name, last_name, user_name, email)
    return jsonify(result)


@app.route("/user/<user_name>", methods=["DELETE"])
def delete_user(user_name):
    result = user_controller.delete_user(user_name)
    return jsonify(result)


@app.route("/user/<user_name>", methods=["GET"])
def get_by_user_name(user_name):
    user = user_controller.get_by_user_name(user_name)
    return jsonify(user)


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.debug = False
    app.run(host='0.0.0.0', port=8000, debug=False)