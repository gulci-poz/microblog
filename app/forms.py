from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


# importowanie rozszerzeń za pomocą flask.ext.<extension>
# jest deprecated

# formularz dziedziczy z klasy Form,
# pola formularzy definiujemy jako zmienne klasy
# Flask-WTF pełni rolę wrappera dla formularzy WTForms

# pola będą wyrenderowane za pomocą field objects
# (referujemy do argumentu szablonu {{ form.field_name }}
# podanego w widoku)

# przycisk submit nie niesie żadnych danych,
# więc nie definiujemy go tutaj, tylko w szablonie
class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
