from flask import Flask

app = Flask(__name__)

# import na końcu, żeby uniknąć cyklicznych referencji (zmienna app)
# pyCharm chce importów na początku pliku

# widoki to handlery (funkcje), które odpowiadają na żądania
# każda taka funkcja mapuje do jednego lub więcej żądań url

from app import views
