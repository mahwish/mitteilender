from pyck.forms import Form
from wtforms import TextField, TextAreaField, validators


class EmailForm(Form):
    
    item_value = TextField('Email Address', [validators.Length(min=6, max=35),
                                        validators.Email(message="Invalid email format")])
    item_name = TextField('Item Name', [validators.required("Subject cannot be empty")])
   
    
