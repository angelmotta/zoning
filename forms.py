from flask_wtf import Form
from wtforms.fields import TextAreaField, TextField, SelectField, SubmitField
from wtforms import validators, ValidationError

class wwnForm(Form):
    host = TextField('Hostname Lpar', [validators.DataRequired("Please Enter the Server Name")])
    vios = SelectField('VIOS', choices=[('viochp11_12', 'VIOCHP11_12'), ('violmp11_12', 'VIOLMP11_12'), ('viochp08_09', 'VIOCHP08_09')])
    wwn = TextAreaField('Enter your wwns', [validators.Length(min=56, max=56, message="Enter 4 lines with your WWNs")])
    submit = SubmitField('Zoning')
