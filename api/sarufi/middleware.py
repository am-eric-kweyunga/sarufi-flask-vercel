from flask import Flask, jsonify

def create_app():
    
    app = Flask(__name__)
    
    @app.route('/')
    def sarufi_middleware_index_route():
        return jsonify({'message': 'Welcome to Sarufi middleware!'})
    
    return app