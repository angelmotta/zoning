from flask_wtf import Form
from wtforms.fields import TextAreaField, TextField, SelectField, SubmitField
from wtforms import validators, ValidationError

class wwnForm(Form):
    host = TextField('Hostname Lpar', [validators.DataRequired("Please Enter the Server Name")])
    vios = SelectField('VIOS', choices=[('viochp11_12', 'VIOCHP11_12'), ('violmp11_12', 'VIOLMP11_12'), ('viochp08_09', 'VIOCHP08_09'), ('violmp08_09', 'VIOLMP08_09')])
    wwn = TextAreaField('Enter your wwns', [validators.Length(min=64, message="Enter at least 4 lines with your WWNs")])
    submit = SubmitField('Zoning')

#Modificar por el nombre del PureFlex
class wwnFormPure(Form):
    host = TextField('Hostname Lpar', [validators.DataRequired("Please Enter the Server Name")])
    vios = SelectField('VIOS', choices=[('pvioschp01', 'PVIOSCHP01'), ('pvioschd01', 'PVIOSCHD01'), ('pvioschd03', 'PVIOSCHD03'), ('pvioslmp01', 'PVIOSLMP01'), ('pvioslmd01', 'PVIOSLMD01'), ('pvioslmd03', 'PVIOSLMD03'), ('pvioslmd05', 'PVIOSLMD05')])
    wwn = TextAreaField('Enter your wwns', [validators.Length(min=32, message="Enter at least 2 lines with your WWNs")])
    submit = SubmitField('Zoning')
