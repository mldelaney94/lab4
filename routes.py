#!/usr/bin/python3
from flask import Flask
from server import app
@app.route("/")
def index():
    return "<h1>Oh</h1>"
