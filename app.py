from flask import Flask

# Create a Flask application
instance = Flask(__name__)

# Add a single endpoint
@instance.route("/")
def hello_fnr():
    return "Goodbye World"

if __name__ == '__main__':
    instance.run()