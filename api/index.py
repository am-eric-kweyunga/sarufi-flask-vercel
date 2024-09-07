from sarufi.middleware import create_app
from flask import jsonify

app = create_app()

@app.route('/')
def sarufi_middleware_index_route():
    return jsonify({'message': 'Welcome to Sarufi middleware!'})

if __name__ == '__main__':
    app.run(debug=True)