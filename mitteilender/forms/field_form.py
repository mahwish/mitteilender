from pyck.forms import Form
from wtforms import SelectField, TextField, TextAreaField, validators


class FieldForm(Form):

    fieldd_type = SelectField('Type',choices= [('text', 'text'),('cell', 'cell'),('image', 'image'),('map', 'map')])
    # = SelectField('Type')
    field_name = TextField()

   
    #field_type = SelectField('Type')
    #description = TextAreaField("Description", [validators.required("Description cannot be empty")])
 
