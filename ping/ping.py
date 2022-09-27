import os
from flask import Flask, jsonify, request 
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message':'Page Not Here'}), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message':'Something is Broke'}), 500

@app.route('/ping', methods=['GET'])
def index():
    return jsonify({'message':'Running...'})