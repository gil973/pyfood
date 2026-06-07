"""
PyFood - Main Flask Application
Linux System Performance Monitor & Optimizer with Web Dashboard
"""

import os
import sys
from flask import Flask, render_template, jsonify
from flask_cors import CORS

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import (
    DEBUG, HOST, PORT, SECRET_KEY, LOG_LEVEL, CORS_ORIGINS,
    DATA_DIR, REPORT_DIR, CACHE_DIR
)
from pyfood.api.routes import api_bp
from pyfood.utils.logger import setup_logger

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

app.config['DEBUG'] = DEBUG
app.config['SECRET_KEY'] = SECRET_KEY

logger = setup_logger(__name__, LOG_LEVEL)

CORS(app, resources={r"/api/*": {"origins": CORS_ORIGINS}})

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/performance')
def performance():
    return render_template('performance.html')


@app.route('/processes')
def processes():
    return render_template('processes.html')


@app.route('/optimizer')
def optimizer():
    return render_template('optimizer.html')


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': str(error)}), 404


@app.errorhandler(500)
def server_error(error):
    logger.error(f"Server error: {error}")
    return jsonify({'error': 'Server error', 'message': str(error)}), 500


@app.before_request
def before_request():
    pass


@app.after_request
def after_request(response):
    response.headers['X-PyFood-Version'] = '1.0.0'
    return response


if __name__ == '__main__':
    logger.info(f"Starting PyFood on {HOST}:{PORT}")
    try:
        app.run(
            host=HOST,
            port=PORT,
            debug=DEBUG,
            use_reloader=DEBUG,
            threaded=True
        )
    except KeyboardInterrupt:
        logger.info("PyFood stopped by user")
    except Exception as e:
        logger.error(f"Error starting PyFood: {e}")
        sys.exit(1)
