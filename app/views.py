from app import app
from flask import flash
from flask import redirect
from flask import render_template
from flask import send_from_directory
import os
from .forms import LoginForm


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


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # mamy pustą akcję w formularzu, na submit robimy walidację
    # każde pole, które ma dołączony walidator będzie miało
    # dołączoną listę z komunikatami błędów form.<field_name>.errors
    if form.validate_on_submit():
        # get_flashed_messages() z szablonu
        # po pobraniu wiadomości usuwa je
        # wiadomości pojawią się również na stronie z redirect()
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
