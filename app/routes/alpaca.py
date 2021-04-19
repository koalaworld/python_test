from random import randint

from flask import request, jsonify

from app import app
from app.controller.alpaca_controller import alpaca_controller

@app.route('/')
@app.route('/<string:sel>')
def index(sel="ALL"):
	return alpaca_controller.index(sel)

@app.route('/profile/<name>')
def profile(name):
    return alpaca_controller.profile(name)

@app.route('/api/alpaca', methods=['POST'])
def api_alpaca():
    if request.method != 'POST':
    	return jsonify({errorMessage: 'Bad Request',success: False})
    body = request.json
    data = alpaca_controller.create(body['name'], body['displayName'], body['bio'],body['age'], body['hobbies'], body['contact'], body['sex'])
    return jsonify(data)
