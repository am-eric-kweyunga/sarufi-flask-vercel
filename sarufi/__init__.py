from flask import Flask, jsonify, request

def create_app():
    
    app = Flask(__name__)
    
    #####################################################################################################
    # Adding Blueprints from blueprints
    #####################################################################################################
    from sarufi.middleware import sarufi_middleware

    # Initialize Flask app
    app = Flask(__name__)


    # App routes
    @app.route("/")
    def sarufi_middleware_index_route():
        return jsonify({"text": "value"})


    #######################################################################################################
    # Adding Blueprints
    #######################################################################################################
    app.register_blueprint(sarufi_middleware, url_prefix="/api/v1/sarufi_middleware")
    
    return app