from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from pyck.forms import model_form
from wtforms.widgets.core import Select
from wtforms import SelectField
from ..models import DBSession, Info_projects, project_items
    
from ..forms import ContactForm, NewForm, ItemForm, MoreItemsForm
    
from pyck.controllers import CRUDController
import os

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
    ret = {}
    for p in plist:
        ret[p.name] = p.ip_id

    return ret


@view_config(route_name='json_project_details', renderer='json')
def project_details(request):
    
    project_name = request.matchdict['pname']
    P = DBSession.query(Info_projects).filter_by(name=project_name).first()
    if not P:
        return HTTPNotFound(message="Project %s does not exist" % project_name)

    PIs = DBSession.query(project_items).filter_by(infoproject_id=P.ip_id).order_by(project_items.display_order)
    ret = []
    
    for PI in PIs:
        ret.append(dict(item_name=PI.item_name, item_type=PI.item_type, display_order=PI.display_order, parent_item=PI.parent_item, email=PI.email, cell_num=PI.cell_num, landline=PI.landline))
    
    return ret
  
@view_config(route_name='dbshow', renderer="dbshow.mako")   
def my_savings(request):
  
  
  
  
    var1=request.POST['name1']
    var2=request.POST['name2']
    model=Info_projects(name=var1, ip_description=var2)
    DBSession.add(model)
    acc2 = DBSession.query(Info_projects).all()
    
    return {'acc2':acc2}  


@view_config(route_name='image', renderer='json')
def image(request):
    p = request.static_url('/home/mahwish/mitteilender/mitteilender/static/komodo1.png')
    import webbrowser
    webbrowser.open(p)
  
  
@view_config(route_name='mahi', renderer="mahi.mako")   
def my_sav(request):
  return {}

@view_config(route_name='project_list', renderer='project_list.mako')   
def my_func(request):
    plist = DBSession.query(Info_projects).all()
    
    return {'plist':plist}

@view_config(route_name='more_items', renderer="more_items.mako")
def more_items_form(request):

            f = MoreItemsForm(request.POST)   # empty form initializes if not a POST request
            if 'POST' == request.method and 'form.submitted' in request.params:
	      if f.validate():
              #fff = os.path.realpath(f.image_data.data)
               fff = request.POST['image_data'].file.read()
              #y   = f.image_data.data
              #cwd = os.getcwd()
              #path = cwd + '/images'
              #path = os.path.join(cwd , '/images')
              
              #request.session.flash(path)
               path = '/home/agha/Documents/fyp/mitteilender/mitteilender/images'
               open(os.path.join(path, request.POST['image_data'].filename), 'w').write(fff)
              
              
             
               import webbrowser
               webbrowser.open(path)
             
            return {'more_items_form': f}


@view_config(route_name='item', renderer="item.mako")
def item_form(request):

    f = ItemForm(request.POST)   # empty form initializes if not a POST request

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

    return {'item_form': f}


 
