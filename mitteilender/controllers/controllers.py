from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from pyck.forms import model_form
from wtforms.widgets.core import Select
from wtforms import SelectField
from ..models import DBSession, Info_projects
    
from ..forms import ContactForm, NewForm, ItemForm
    
from pyck.controllers import CRUDController

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






#@view_config(route_name='new', renderer="new.mako")
#def new_form(request):

 #   f = NewForm(request.POST)   # empty form initializes if not a POST request

  #  if 'POST' == request.method and 'form.submitted' in request.params:
   #     if f.validate():
            #TODO: Do email sending here.
    #        P = Info_projects()
        
     #       f.populate_obj(P)
      #      DBSession.add(P)

       #     request.session.flash("Your message has been sent!")
        #    return HTTPFound(location=request.route_url('dbshow'))

    #return {'new_form': f}
  
@view_config(route_name='dbshow', renderer="dbshow.mako")   
def my_savings(request):
  
  
  
  
    var1=request.POST['name1']
    var2=request.POST['name2']
    model=Info_projects(name=var1, ip_description=var2)
    DBSession.add(model)
    acc2 = DBSession.query(Info_projects).all()
    
    return {'acc2':acc2}  
  
  
  
  
  
  
  
  
@view_config(route_name='mahi', renderer="mahi.mako")   
def my_sav(request):
  return {}

@view_config(route_name='project_list', renderer='project_list.mako')   
def my_func(request):
    plist = DBSession.query(Info_projects).all()
    
    return {'plist':plist}
  

    







@view_config(route_name='item', renderer="item.mako")
def item_form(request):

    f = ItemForm(request.POST)   # empty form initializes if not a POST request

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

    return {'item_form': f}


