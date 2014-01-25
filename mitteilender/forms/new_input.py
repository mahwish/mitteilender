from pyck.forms import Form
from wtforms import TextField, TextAreaField, validators


class AddInputForm(Form):
    input_name = TextField('Name',[validators.required("Name cannot be empty")])
    success_message = TextField('Message',[validators.required("Name cannot be empty")])
    
   
