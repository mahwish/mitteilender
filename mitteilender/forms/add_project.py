from pyck.forms import Form
from wtforms import TextField, TextAreaField, validators


class AddProjectForm(Form):
    name = TextField('Name',[validators.required("Name cannot be empty")])
    
    ip_description = TextAreaField('Description', [validators.required("Description cannot be empty")])
