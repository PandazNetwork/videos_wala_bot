from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from PandazNetwork'

if __name__ == "__main__":
    # Use the PORT environment variable provided by Render
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 for local testing
    app.run(host='0.0.0.0', port=port)  # Bind to 0.0.0.0 for Render compatibility
