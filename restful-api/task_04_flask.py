#!/usr/bin/python3
"""casual flask server"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    print("Welcome to the Flask API!")

@app.route("/data")
def data():
    return jsonify(list(users.keys))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user_info(username):
    user = user.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    }), 200

if __name__ == "__main__":
    run()
