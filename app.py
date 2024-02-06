from flask import Flask

# Create a Flask application
instance = Flask(__name__)

# Add a single endpoint
@instance.route("/")
def hello_fnr():
    return "Goodbye World"

instance.route("/oh")
def oh_world():
    return "oh world"

if __name__ == '__main__':
    instance.run()
