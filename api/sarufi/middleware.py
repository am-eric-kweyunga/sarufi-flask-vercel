from flask import Flask, jsonify

def create_app():
    
    app = Flask(__name__)
    
    return app