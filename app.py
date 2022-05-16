import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/intro')
def hello():
    return 'Hello, I am running from a container.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    