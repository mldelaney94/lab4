#!/bin/usr/python3
from flask import Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "High"
