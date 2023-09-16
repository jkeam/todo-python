from flask import Flask, jsonify
from os import environ
from requests import get

app = Flask(__name__)
ROOT_URL = 'https://jsonplaceholder.typicode.com/todos'

@app.route('/health')
def health():
    return jsonify({'message': 'healthy'})

@app.route('/')
def todos():
    return jsonify(get(ROOT_URL).json())

@app.route('/<id>')
def todo(id):
    return jsonify(get(f"{ROOT_URL}/{id}").json())

if __name__ == '__main__':
   port = environ.get('PORT', 8080)
   app.run(debug=True, host='0.0.0.0', port=int(port))
