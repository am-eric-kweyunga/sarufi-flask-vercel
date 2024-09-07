from flask import Flask, jsonify

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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
