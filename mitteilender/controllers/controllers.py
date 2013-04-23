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
    return {'one': one, 'project': 'mitteilender'}


@view_config(route_name='contact', renderer="contact.mako")
def contact_form(request):

    f = ContactForm(request.POST)   # empty form initializes if not a POST request

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

    return {'contact_form': f}






@view_config(route_name='new', renderer="new.mako")
def new_form(request):

    f = NewForm(request.POST)   # empty form initializes if not a POST request

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.
            P = Info_projects()
        
            f.populate_obj(P)
            DBSession.add(P)
            categories = DBSession.query(Info_projects.ip_id, Info_projects.name).all()

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

    return {'new_form': f}







@view_config(route_name='item', renderer="item.mako")
def item_form(request):

    f = ItemForm(request.POST)   # empty form initializes if not a POST request

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

    return {'item_form': f}


