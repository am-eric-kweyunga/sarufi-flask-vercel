from flask import  Flask,jsonify

app = Flask(__name__)

@app.route('/')
def sarufi_middleware_index_route():
    return jsonify({'message': 'Welcome to Sarufi middleware!'})

if __name__ == '__main__':
    app.run(debug=True)