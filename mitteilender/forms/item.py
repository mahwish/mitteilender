from pyck.forms import Form
from wtforms import TextField, TextAreaField, validators


class ItemForm(Form):
    name = TextField('Name',[validators.required("Name cannot be empty")])
  
