import os
from flask import Flask
from flask import send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to Flask app home page!'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()
