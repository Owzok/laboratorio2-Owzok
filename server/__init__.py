from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from models import setup_db, Example

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, origins=['https://utec.edu.pe'], max_age = 10)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,OPTIONS')
        return response




    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 500,
            'message': 'Internal Server error'
        }), 500

    @app.errorhandler(422)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 422,
            'message': 'Unprocessable entity'
        }), 422

    @app.route('/')
    def index():
        return 'Hello API'

    return app