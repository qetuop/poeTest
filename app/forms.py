from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField, TextField

class LoginForm(FlaskForm):
    account = StringField('Account')
    poessid = StringField('POESSID') # POESESSID de4c695e9a693a94b563a1727233c7b7
    league = SelectField(u'League')
    submit = SubmitField('Submit')
    tabs = StringField('Verify')

