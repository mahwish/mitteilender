from pyck.forms import Form
from wtforms import TextField, TextAreaField, validators, FileField


class MoreItemsForm(Form):
 
  images_title = TextField('Image',[validators.required("Image cannot be empty")])
  #email = TextField('Email',[validators.required("Email cannot be empty")]) 
  email = TextField('Email Address', [validators.Length(min=6, max=35),
                                        validators.Email(message="Invalid email format")])
  landline = TextField('Landline',[validators.required("Landline number cannot be empty")])
  cell_num = TextField('CEll number',[validators.required("Cell number cannot be empty")])

  images_title = TextField('Image', [validators.Length(min=10, max=12),validators.required("Image cannot be empty")])
  image_data = FileField()

