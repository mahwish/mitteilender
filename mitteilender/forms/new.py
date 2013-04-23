from pyck.forms import Form
from wtforms import TextField, TextAreaField, validators


class NewForm(Form):
    name = TextField('Name',[validators.required("Name cannot be empty")])
    
    description = TextAreaField('Description', [validators.required("Description cannot be empty")])
