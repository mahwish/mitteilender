from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from pyck.forms import model_form
from wtforms.widgets.core import Select
from wtforms import SelectField
from ..models import DBSession, Info_projects, project_items, db_recordss, db_itemss

from ..forms import ContactForm, NewForm, ItemForm, MoreItemsForm, FieldForm

from pyck.controllers import CRUDController
import os
import csv


class Info_projectsCRUDController(CRUDController):
    model = Info_projects
    db_session = DBSession

    


@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    one = None
    return {'one': one, 'project': 'designer'}


@view_config(route_name='contact', renderer="contact.mako")
def contact_form(request):

    f = ContactForm(request.POST)   # empty form initializes if not a POST request

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

    return {'contact_form': f}


@view_config(route_name='json_project_list', renderer='json')
def json_proj_list(request):
    plist = DBSession.query(Info_projects).all()
    return plist


def get_items(project_id, parent_item):
    ret = []

    items = DBSession.query(project_items).filter_by(infoproject_id=project_id, parent_item=parent_item).order_by(project_items.display_order)
    for PI in items:
        if 'section' == PI.item_type.lower():
            PI.subitems = get_items(project_id, PI.item_name)

        ret.append(PI)

    return ret


@view_config(route_name='json_project_details', renderer='json')
def project_details(request):

    project_name = request.matchdict['pname']
    P = DBSession.query(Info_projects).filter_by(name=project_name).first()
    if not P:
        return HTTPNotFound(message="Project %s does not exist" % project_name)

    project_details = get_items(P.ip_id, '')

    return project_details


@view_config(route_name='project_list', renderer='project_list.mako')
def project_list(request):
    projects = DBSession.query(Info_projects).all()
    return {'projects': projects}

@view_config(route_name='upload_image', renderer='upload_image.mako')
def upload_image(request):

    project_name = request.matchdict['pname']

    if 'POST' == request.method:
        item_id = int(request.POST['item_id'])
        image_data = request.POST['image_file'].file.read()
        project_item = DBSession.query(project_items).filter_by(pi_id=item_id).first()
        if not project_item:
            return HTTPNotFound(message="Project item does not exist")

        current_folder = os.path.dirname(__file__)
        filename = "../static/uploaded_images/%i.jpg" % item_id
        complete_path = os.path.abspath(os.path.join(current_folder, filename))
        #print(complete_path)
        open(complete_path, 'wb').write(image_data)
        project_item.item_value = 'static/uploaded_images/%i.jpg' % item_id
        request.session.flash("Image uploaded!")
        
    P = DBSession.query(Info_projects).filter_by(name=project_name).first()
    if not P:
        return HTTPNotFound(message="Project %s does not exist" % project_name)

    image_items = DBSession.query(project_items).filter_by(infoproject_id=P.ip_id, item_type='image').order_by(project_items.display_order)

    return {'project': P, 'image_items': image_items}
@view_config(route_name='upload_f', renderer='upload_f.mako')
def upload_file(request):

    project_name = request.matchdict['pname']
    records = []
    header = False
    fields = []
    if 'POST' == request.method:
        r = csv.reader(request.POST['csv_file'].file)
       
        for row in r:
	    
	    #print(row)
	    if not header:
	        header= row
	    records.append(row)
	        
	        #continue
	        
	  
	    #print(records)
	        
	        
	        #continue
	    #records.append(row)
	    #print(records)
	    
        request.session.flash("csv file uploaded!")
        #print(fields)
        print(records)
        #return {'fields': fields, 'records': records}
        
 
    P = DBSession.query(Info_projects).filter_by(name=project_name).first()
    if not P:
        return HTTPNotFound(message="Project %s does not exist" % project_name)

    #image_items = DBSession.query(project_items).filter_by(infoproject_id=P.ip_id).order_by(project_items.display_order)

    return {'project': P, 'fields': fields, 'records': records}


@view_config(route_name='field_type', renderer="field_type.mako")   
def my_pro(request):  
    #project_name = request.matchdict['pname']
    f_form = FieldForm(request.POST)
    names = DBSession.query(db_itemss.field_name).all()
    
    
    f_form.field_name = names
    #print(f_form)
    types=['text','cell','image','email','map']
    
    f_form.field_type.choices = types
    print(f_form.field_type.choices)
    
    if "POST" == request.method and f_form.validate():

        
     #   P = Books()
        #request.session.flash({Books.name})
      #  product_form.populate_obj(P)
       # DBSession.add(P)
        
        request.session.flash("Books Added Successfully!")
        #return HTTPFound(location=request.route_url('home'))
    
    
    return {'f_form': f_form,'f_form.field_type.choices':f_form.field_type.choices,'post_url': request.route_url('field_type')}
    #P = DBSession.query(Info_projects).filter_by(name=project_name).first()
    #if not P:
     #   return HTTPNotFound(message="Project %s does not exist" % project_name)
 
    #return{'f_form':f_form}





	
#@view_config(route_name='show_f', renderer='show_f.mako')
#def show_csv(request):
  
 # reader = csv.reader(open("/home/mahwish/mitteilender/mitteilender/static/uploaded_csv/57.csv", "rb"))
 # for row in reader:
   # print row
  #  return{'reader':reader}
    
  
		
 

#@view_config(route_name='upload_file', renderer='upload_file.mako')
#def upload_file(request):
 #  project_name = request.matchdict['pname']

  #  if 'POST' == request.method:
   #     item_id = int(request.POST['item_id'])
    #    image_data = request.POST['upload_file'].file.read()
     #   project_item = DBSession.query(project_items).filter_by(pi_id=item_id).first()
      #  if not project_item:
       #     return HTTPNotFound(message="Project item does not exist")

        #current_folder = os.path.dirname(__file__)
        #filename = "../static/uploaded_images/%i.csv" % item_id
        #complete_path = os.path.abspath(os.path.join(current_folder, filename))
        #print(complete_path)
        #open(complete_path, 'wb').write(image_data)
        #project_item.item_value = 'static/uploaded_images/%i.csv' % item_id
        #request.session.flash("Image uploaded!")
        
    #P = DBSession.query(Info_projects).filter_by(name=project_name).first()
    #if not P:
     #   return HTTPNotFound(message="Project %s does not exist" % project_name)

    #image_items = DBSession.query(project_items).filter_by(infoproject_id=P.ip_id, item_type='image').order_by(project_items.display_order)
#return {'project': P, 'image_items': image_items}
