from pyck.forms import Form
from wtforms import TextField, TextAreaField, validators


class AddTextForm(Form):
    
    
    item_name = TextField('Text title', [validators.required("Title cannot be empty")])
    item_value =  TextAreaField('Description', [validators.required("Description cannot be empty")])

   
   
    
