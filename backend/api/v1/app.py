#!/usr/bin/env/python3.9
""" Entry point for the application """
from flask import Flask

app = Flask(__name__)


# Test route
@app.route('/')
def home() -> None:
    return ("Hello, Welcome!")

if __name__ == "__main__":
    app.run(debug=True)