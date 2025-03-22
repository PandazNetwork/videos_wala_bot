from bot import Bot
from flask import Flask, jsonify
import threading

# Initialize Flask app
app = Flask(__name__)

# Define the root endpoint
@app.route("/")
def home():
    return jsonify({"message": "Welcome To PandazNetwork"})

# Function to run the Flask app
def run_flask():
    app.run(host="0.0.0.0", port=8080)
Bot().run()
