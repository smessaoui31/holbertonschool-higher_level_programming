from flask import Flask
from flask import jsonify
from flask import request
import json


app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    usernames = [username for username in users.keys()]
    return jsonify(usernames)

@app.route("/users/<username>")
def get_user(username):
    if username in users.keys():
        user = users[username]
        return jsonify(user)
    else :
        error = {"error": "User not found"}
        return jsonify(error), 404










if __name__ == "__main__":
    app.run()