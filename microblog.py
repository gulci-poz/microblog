from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to Flask app home page!'


if __name__ == '__main__':
    app.run()
