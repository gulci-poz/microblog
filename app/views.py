from app import app
import os
from flask import send_from_directory


@app.route('/')
@app.route('/index')
def index():
    return "Hello, microblog app!"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
