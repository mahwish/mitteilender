from pyck.forms import Form
from wtforms import SelectField, TextField, TextAreaField, validators


class FieldForm(Form):
    field_type = SelectField('Type', coerce=str)
    #field_type = SelectField('Type')
    field_name = TextField('Field Name')
    #description = TextAreaField("Description", [validators.required("Description cannot be empty")])
 
