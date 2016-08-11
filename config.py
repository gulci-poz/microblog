import os

basedir = os.path.abspath(os.path.dirname(__file__))

# zapobieganie cross-site request forgery
# powinno być domyślnie włączone w Flask-WTF
# w formularzu funkcja form.hidden_tag() (Flask-WTF)
# generuje ukryte pole (WTForms)
# musimy mieć to wywołanie w każdym formularzu
WTF_CSRF_ENABLED = True

# token kryptograficzny do walidacji formularza
# potrzebny kiedy zapobieganie CSRF jest włączone
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://accounts.google.com'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_TRACK_MODIFICATIONS = False
