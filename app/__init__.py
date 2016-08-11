from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# import na końcu, żeby uniknąć cyklicznych referencji (zmienna app)
# pyCharm chce importów na początku pliku

# widoki to handlery (funkcje), które odpowiadają na żądania
# każda taka funkcja mapuje do jednego lub więcej żądań url

from app import views
from app import models
