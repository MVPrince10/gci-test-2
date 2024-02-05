from flask import Flask

# Create a Flask application
instance = Flask(__name__)

# Add a single endpoint for 'Hello World'
@instance.route("/hello")
def hello():
    return "Hello World"

# Add another endpoint for 'Goodbye World'
@instance.route("/goodbye")
def goodbye():
    return "Goodbye World"

if __name__ == '__main__':
    instance.run()
