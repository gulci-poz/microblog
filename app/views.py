from app import app
from flask import render_template
from flask import send_from_directory
import os


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'gulci'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

    # return '''
    # <html>
    #     <head>
    #         <title>Microblog Home Page</title>
    #     </head>
    #     <body>
    #         <h1>Hello, ''' + user['nickname'] + '''</h1>
    #     </body>
    # </html>
    # '''


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
