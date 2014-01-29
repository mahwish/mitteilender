from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from pyck.forms import model_form
from wtforms.widgets.core import Select
from wtforms import SelectField
from ..models import DBSession, Info_projects, project_items, db_recordss, db_itemss,user_input,input_fields

from ..forms import ContactForm, NewForm, ItemForm, MoreItemsForm, FieldForm, EmailForm,AddProjectForm,AddInputForm,AddTextForm

from pyck.controllers import CRUDController
import os
import csv
import webbrowser


class Info_projectsCRUDController(CRUDController):
    model = Info_projects
    db_session = DBSession

    


@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    one = None
    return {'one': one, 'project': 'Mitteilender'}


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

@view_config(route_name='add_project', renderer='add_project.mako')
def add_project(request):
    add_form = AddProjectForm(request.POST)
    
    
    
    
    
    if "POST" == request.method and add_form.validate():
      
      
      P= Info_projects()
      
      
      
      add_form.populate_obj(P)
      DBSession.add(P)
      DBSession.flush()
      request.session.flash("Project added Successfully !!")
      return HTTPFound(location=request.route_url('home'))
    return{'add_project':add_form}
      
@view_config(route_name='add_project_item')
def add_project_item(request):
    project_name = request.matchdict['pname']
    item_type = request.matchdict['item_type']
    item_id=1
    
    
    print(project_name)
    p_id = DBSession.query(Info_projects.ip_id).filter_by(name=project_name).one()
    print("ID")
    i=str(p_id[0])
    print(i)
    List=[]
    d_order =DBSession.query(project_items).filter_by(infoproject_id=i).filter_by(parent_item='None').all()
     
      
    for d in d_order:
      if(d.parent_item=='None'):
        List.append((d.item_name))
      
    print("display_order********************************************") 
    #print(display_order)
    display_order=len(List)
   
    print(List)  
    display_order =display_order+1
    print(display_order)
    parent_item=[]
    for sec in DBSession.query(project_items).filter_by(item_type='section').filter_by(infoproject_id=i).all():
      d={}
      d['sec_name']=str(sec.item_name)
      d['sec_id']=int(sec.pi_id)
      
      parent_item.append(d)
      
    print("llllllllllllllllllllllllllllllllllllllllllll")
    print(parent_item)
    for i_id in DBSession.query(project_items.pi_id).all():
      #print("item ID")
      
      item_id=i_id[0]
    print("item ID")  
   # print(str(i_id[0]))
   
    item_id =item_id+1  
      
      
    
    
    print("oooooooooooooooooooooooooooo")
  
    if "POST"==request.method:
      if(item_type=='Contact'):
	Contact=project_items()
	Contact.parent_item='None'
	Contact.infoproject_id=i
	Contact.pi_id=item_id
	Contact.display_order=display_order
	Contact.item_value='None'
	Contact.item_name=(request.POST['contact_name'])
	Contact.item_type='Section'
	DBSession.add(Contact)
	DBSession.flush()
	if(request.POST['cell_name']==""):
	  I=project_items()
	  I.item_name=(request.POST['landline_name'])
	  I.item_value=(request.POST['landline_numer'])
          I.item_type='Landline'
          I.display_order=1
          I.parent_item=item_id
          I.infoproject_id=i
          I.pi_id=item_id+1
          DBSession.add(I)
          DBSession.flush()
          request.session.flash("Contact Item added successfully")
	  return HTTPFound(location=request.route_url('show_item',item_id=item_id+1))
	elif(request.POST['landline_name']==""):
	  I=project_items()
	  I.item_name=(request.POST['cell_name'])
	  I.item_value=(request.POST['cell_number'])
          I.item_type='Cell'
          I.display_order=1
          I.parent_item=item_id
          I.infoproject_id=i
          I.pi_id=item_id+1
          DBSession.add(I)
          DBSession.flush()
          request.session.flash("Contact Item added successfully")
	  return HTTPFound(location=request.route_url('show_item',item_id=item_id+1))
	else:
	  C=project_items()
	  C.item_name=(request.POST['cell_name'])
	  C.item_value=(request.POST['cell_number'])
          C.item_type='Cell'
          C.display_order=1
          C.parent_item=item_id
          C.infoproject_id=i
          C.pi_id=item_id+1
          DBSession.add(C)
          DBSession.flush()
          L=project_items()
	  L.item_name=(request.POST['landline_name'])
	  L.item_value=(request.POST['landline_number'])
          L.item_type='Landline'
          L.display_order=2
          L.parent_item=item_id
          L.infoproject_id=i
          L.pi_id=item_id+2
          DBSession.add(L)
          DBSession.flush()
          request.session.flash("Contact Item added successfully")
	  return HTTPFound(location=request.route_url('show_item',item_id=item_id+1))
	  
	
	
	
    
    
    
    
    
    return{'pname':projectitem_id,'item_id':item_id}

  
        
        
       
        
        
    return {'add_project':add_form}
@view_config(route_name='contact_details', renderer='contact_details.mako')
def contact_details(request):
    project_name = request.matchdict['pname']
    contact_name = request.matchdict['cname']
    p_id = DBSession.query(Info_projects.ip_id).filter_by(name=project_name).one()
    print("ID")
    i=str(p_id[0])
    print(i)
    item_id=0
   
    for i_id in DBSession.query(project_items.pi_id).all():
      #print("item ID")
      
      item_id=i_id[0]
    print("item ID")  
   # print(str(i_id[0]))
   
    #item_id =item_id+1
    if "POST" == request.method:
     
      
      if(contact_name=='cell'):
        
        cell_num= (request.POST['cell_number'])
        cell_name= (request.POST['cell_name'])
	I=project_items()
	I.item_name=cell_name
	I.item_value=cell_num
        I.item_type='Cell'
        I.display_order=1
        I.parent_item=item_id
        I.infoproject_id=i
        I.pi_id=item_id+1
        DBSession.add(I)
        DBSession.flush()
        request.session.flash("Cell number added successfully")
	return HTTPFound(location=request.route_url('contact_details',pname=project_name,cname='landline'))
        
      elif(contact_name=='landline'):
	 
	landline_num= (request.POST['landline_number'])
        landline_name= (request.POST['landline_name'])
	I=project_items()
	I.item_name=landline_name
	I.item_value=landline_num
        I.item_type='Landline'
        I.display_order=2
        I.parent_item=item_id
        I.infoproject_id=i
        I.pi_id=item_id+1
        DBSession.add(I)
        DBSession.flush()
        request.session.flash("Landline number added successfully")
	return HTTPFound(location=request.route_url('contact_details',pname=project_name,cname='cell'))
      else:
	request.session.flash("Contact item added successfully")
	return HTTPFound(location=request.route_url('add',pname=project_name))
	
	
      
      
      
      
    
    return{'pname':project_name,'cname':contact_name}
    
    
    
   
@view_config(route_name='contact_item', renderer='contact_item.mako')
def contact_item(request):
    project_name = request.matchdict['pname']
    project_name = request.matchdict['pname']
    
    p_id = DBSession.query(Info_projects.ip_id).filter_by(name=project_name).one()
    print("ID")
    i=str(p_id[0])
    print(i)
    item_id=0
   
    for i_id in DBSession.query(project_items.pi_id).all():
      #print("item ID")
      
      item_id=i_id[0]
    print("item ID")  
   # print(str(i_id[0]))
   
    item_id =item_id+1
    print(item_id)
   
    List=[]
    d_order  =DBSession.query(project_items).filter_by(infoproject_id=i).all()
     
      
    for d in d_order:
      List.append((d.display_order))
      
    print("display_order********************************************") 
    #print(display_order)
    display_order=len(List)
   
      
    display_order =display_order+1
   
    if "POST" == request.method:
       contact_name = (request.POST['contact_name'])
     
       contact=project_items()
       
       contact.item_name=contact_name
       contact.item_type='Section'
       
       contact.display_order=display_order
       contact.parent_item='None'
       contact.infoproject_id=i
       contact.pi_id=item_id
       DBSession.add(contact)
       DBSession.flush()
       return HTTPFound(location=request.route_url('contact_details',pname=project_name,cname=contact.item_name))
       
	 ##return{'project_name':project_name,
	 

       
        
        
      
       
     
       
       
       
    
  
  
    return{'project_name':project_name}
  
  
  
  
@view_config(route_name='text_item', renderer='text_item.mako')
def text_item(request):
    text_form = AddTextForm(request.POST)
    project_name = request.matchdict['pname']
    
    p_id = DBSession.query(Info_projects.ip_id).filter_by(name=project_name).one()
    print("ID")
    i=str(p_id[0])
    print(i)
    item_id=0
   
    for i_id in DBSession.query(project_items.pi_id).all():
      #print("item ID")
      
      item_id=i_id[0]
    print("item ID")  
   # print(str(i_id[0]))
   
    item_id =item_id+1
    print(item_id)
   
    List=[]
    d_order  =DBSession.query(project_items).filter_by(infoproject_id=i).all()
     
      
    for d in d_order:
      List.append((d.display_order))
      
    print("display_order********************************************") 
    #print(display_order)
    display_order=len(List)
   
      
    display_order =display_order+1
   
    parent_item=[]
    for sec in DBSession.query(project_items).filter_by(item_type='Section').filter_by(infoproject_id=i).all():
      d={}
      d['sec_name']=str(sec.item_name)
      d['sec_id']=int(sec.pi_id)
      parent_item.append(d)
    print("llllllllllllllllllllllllllllllllllllllllllll")
    print(parent_item)
      
      
      
    
    
    print("oooooooooooooooooooooooooooo")
  
    if "POST" == request.method and text_form.validate():
      
        
        if(parent_item)==[]:
	  
	   I =project_items()
	   
	   I.item_type='Text'
       
           I.display_order=display_order
           I.parent_item='None'
           I.infoproject_id=i
           I.pi_id=item_id
           p_item='None'
          
        else:
	   
	  
           I =project_items()
           p_item = str(request.POST['p_item'])
           print("ttttttttttttttttttttttttttttt")
	   print(p_item)
           if(p_item=='0'):
	     I.parent_item='None'
	     I.item_type='Text'
             I.parent_item=p_item
             I.pi_id=item_id
             I.display_order=display_order
             I.infoproject_id=i
           else:
           
       
             I.display_order=display_order
           
             I.infoproject_id=i
	   
	     
             I.item_type='Text'
             I.parent_item=p_item
             I.pi_id=item_id
           
       
           
           
             I.infoproject_id=i
           
        
        print("p id ")
        print(I.pi_id)
        #I.pi_id=5
     
      
      
      
        text_form.populate_obj(I)
        DBSession.add(I)
        DBSession.flush()
        request.session.flash("Text item added Successfully !!")
        return HTTPFound(location=request.route_url('show_item',item_id=item_id))
      
      
        
        
       
        
        
    return {'add_text':text_form,'project_name':project_name,'parent_item':parent_item}

  

@view_config(route_name='p_list', renderer='p_list.mako')
def project_list(request):
    projects = DBSession.query(Info_projects).all()
    return {'projects': projects}
  
  

    
@view_config(route_name='view_items', renderer='view_items.mako')
def view(request):
    p=[]
    k=[]
    project_name = request.matchdict['pname']
    project_id=DBSession.query(Info_projects).filter_by(name=project_name).first()
    #request.session.flash(project_name.ip_id)
    #items=DBSession.query(project_items).filter_by(infoproject_id=p_id).first()
    print("isttttttttttttttttt")
    print(project_id.ip_id)
    p_items = DBSession.query(project_items).filter_by(infoproject_id=project_id.ip_id).all()
    for i in p_items:
       p.append(int(i.display_order))
    k=sorted(p)
  
    return {'p_items':p_items,'display_order':k,'pname':project_name}

      #print(p.pi_id)
    
      
      
    
    #exp(p,p_items)
 
  

@view_config(route_name='add', renderer='add.mako')
def add(request):
  project_name = request.matchdict['pname']
  return{'project_name':project_name}

  
@view_config(route_name='section_item', renderer='section_item.mako')
def section(request):
    project_name = request.matchdict['pname']
    print("pname")
    print(project_name)
    
    print("________")
    p_id = DBSession.query(Info_projects.ip_id).filter_by(name=project_name).one()
    print("ID")
    i=str(p_id[0])
    print(i)
    print("****************")
    p_name=[]
   
    print("oooooooooooooooooooooooooooo")
    item_id=0
    for i_id in DBSession.query(project_items.pi_id).all():
      #print("item ID")
      
      item_id=i_id[0]
    print("item ID")  
   # print(str(i_id[0]))
   
    item_id =item_id+1
    print(item_id)
    List=[]
    d_order  =DBSession.query(project_items).filter_by(infoproject_id=i).all()
     
      
    for d in d_order:
      List.append((d.display_order))
      
    print("display_order********************************************") 
    #print(display_order)
    display_order=len(List)
   
      
    display_order =display_order+1
    
    if 'POST' == request.method:
        
        sec_name = (request.POST['name'])
        
        
        print("&&&&&&&&&&&&&")
        print(sec_name)
        I =project_items()
        #request.session.flash(sec_name)
        #request.session.flash(d)
        #request.session.flash(int(i[0]))
        #request.session.flash(item_id)
        I.item_name=sec_name
        I.item_type='Section'
        
        I.parent_item='None'
        
        I.display_order=display_order
        I.pi_id=item_id
        I.infoproject_id=i
        #I.parent_item=0
        #I.pi_id=5
        
        DBSession.add(I)
        DBSession.flush()
        request.session.flash("Section item added Successfully !!")
        return HTTPFound(location=request.route_url('show_item',item_id=item_id))
        #request.session.flash("Added")
        #it.append(D.db_item_id)
        
        
        
      
    

   
    #print(p_name)
    return {'project_name':project_name,'p_name':p_name,'display_order':display_order}
  
  
  
  
  
  
  # pi_id = Column(Integer, primary_key=True)
   # infoproject_id = Column(Integer, ForeignKey(Info_projects.ip_id))
    #item_name = Column(Unicode(200))
    #item_value = Column(Unicode(1000))
    #item_type = Column(Unicode(200))
    #display_order = Column(Unicode(200))
    #parent_item = Column(Unicode(200))

  
  
  

@view_config(route_name='try', renderer='try.mako')
def tryy(request):
   project_name = request.matchdict['pname']
   project_id=DBSession.query(Info_projects).filter_by(name=project_name).first()
   items = DBSession.query(project_items).filter_by(infoproject_id=project_id.ip_id).all()
   item_type='DbItem'
   item_id=[]
   for PI in items:
        item_id.append(PI.pi_id)
   print("idddddddddd")
   print(item_id)
   index=0
   listt=[]
   
   for d_item in DBSession.query(db_itemss).filter_by(projectitem_id=item_id[index]):
     d={}
     d['field_name']=d_item.field_name
     d['dbitem_id']=d_item.projectitem_id
     for d_rec in DBSession.query(db_recordss).filter_by(dbitem_id=d_item.db_item_id):
      
       d['rec_value']=d_rec.db_item_value
     index=index+1
     listt.append(d)
   
   print("listtttttttttttttttttttttttttt")
   print(listt)
   
   return{'p':123}

@view_config(route_name='swap')
def swap(request):
  item_id = request.matchdict['item_id']
  direction = request.matchdict['direction']
  print("PPPPPPPPPPPPPPPPPPPPP")
  print(item_id)
  print(direction)
  request.session.flash(item_id)
  request.session.flash(direction)
  p_idd=DBSession.query(project_items).filter_by(pi_id=item_id).first()
  p_id=int(p_idd.infoproject_id)
  print(p_id)
  o=0
  q =DBSession.query(project_items).filter_by(infoproject_id=p_id).all()
  ii=[]
  p=[]
  bb = DBSession.query(project_items).filter_by(infoproject_id=p_id).all()
  for b in bb:
      ii.append(int(b.pi_id))   
 
	
      
    
  

  if(direction=='up'):
	     
	      
	      
	      curr=DBSession.query(project_items).filter_by(pi_id=item_id).first()
	      current=int(curr.display_order)
	      
	      nextt=current-1
	      print("preeeeeeeeeeeeeeeeeee")
	      print(nextt)
	      nxt=DBSession.query(project_items).filter_by(display_order=nextt).first()
	     
	  
	    
	     
	      curr.display_order=nextt
	      nxt.display_order=current
	  
              return HTTPFound(location=request.route_url('swap_display_order',p_id=p_id))
	     
  elif(direction=='down'):
	     #cur=item_id
	     
	     #var1=item_id+1
	     
	     curr=DBSession.query(project_items).filter_by(pi_id=item_id).first()
	     current=int(curr.display_order)
	     nextt=current+1
	     nxt=DBSession.query(project_items).filter_by(display_order=nextt).first()
	     
	  
	    
	     
	     curr.display_order=nextt
	     nxt.display_order=current
	  
             return HTTPFound(location=request.route_url('swap_display_order',p_id=p_id))	     
	     
  return HTTPFound(location=request.route_url('swap_display_order',p_id=p_id))	     
	     
	    
	    
	      
	   
	      
	      
	 
  
  
	    
	    
	
	
	  
      
  
   
   
  
  
  
@view_config(route_name='swap_display_order', renderer='swap_display_order.mako')
def swap_display_order(request):
    p=[]
    k=[]
    p_id = request.matchdict['p_id']
   
    
    p_items = DBSession.query(project_items).filter_by(infoproject_id=p_id).order_by(project_items.display_order).filter_by(parent_item='None').all()
    
    for i in p_items:
       p.append(int(i.display_order))
    display_order=sorted(p)
    print(display_order)
    first=display_order[0]
    length=len(display_order)
    last=display_order[length-1]
    
    print(first)
    print(last)
    print(")))))))))))))))))))))")
    print(first)
    print(last)
    n=[]
    ii=[]
    bb = DBSession.query(project_items).filter_by(infoproject_id=p_id).all()
    for b in bb:
      ii.append(int(b.pi_id))
      
    print("IIIIIIIIIIIIII")
    print(ii)
  
	    
	    
	
	
	  
      
    return {'p_items':p_items,'first':str(first),'last':str(last),'display_order':display_order,'p_id':p_id}
  
  
  








@view_config(route_name='upload_image', renderer='upload_image.mako')
def upload_image(request):

    project_name = request.matchdict['pname']
    records = []
    header = False
    fields = []
    
    print(project_name)
    p_id = DBSession.query(Info_projects.ip_id).filter_by(name=project_name).one()
    print("ID")
    i=str(p_id[0])
    print(i)
    item_id=0
   
    for i_id in DBSession.query(project_items.pi_id).all():
      #print("item ID")
      
      item_id=i_id[0]
    print("item ID")  
   # print(str(i_id[0]))
   
    item_id =item_id+1
    print(item_id)
   
    List=[]
    d_order  =DBSession.query(project_items).filter_by(infoproject_id=i).all()
     
      
    for d in d_order:
      List.append((d.display_order))
      
    print("display_order********************************************") 
    #print(display_order)
    display_order=len(List)
   
      
    display_order =display_order+1
   
    parent_item=[]
    for sec in DBSession.query(project_items).filter_by(item_type='Section').filter_by(infoproject_id=i).all():
      d={}
      d['sec_name']=str(sec.item_name)
      d['sec_id']=int(sec.pi_id)
      parent_item.append(d)
    print("llllllllllllllllllllllllllllllllllllllllllll")
    print(parent_item)
      
      
      
    
    
    print("oooooooooooooooooooooooooooo")
    if 'POST' == request.method:
      
        
        i_name = (request.POST['name'])
        if(parent_item)==[]:
	  
	   I =project_items()
	   I.item_name=i_name
	   I.item_type='Image'
       
           I.display_order=display_order
           I.parent_item='None'
           I.infoproject_id=i
           I.pi_id=item_id
           p_item='None'
          
        else:
	   
	  
           I =project_items()
           p_item = str(request.POST['p_item'])
           print("ttttttttttttttttttttttttttttt")
	   print(p_item)
           if(p_item=='0'):
	     I.parent_item='None'
	     I.item_type='Image'
             I.parent_item=p_item
             I.pi_id=item_id
             I.display_order=display_order
             I.infoproject_id=i
           else:
           
       
             I.display_order=display_order
           
             I.infoproject_id=i
	   
	     
             I.item_type='Image'
             I.parent_item=p_item
             I.pi_id=item_id
           
       
           
           
             I.infoproject_id=i
           
        
        print("p id ")
        print(I.pi_id)     #I.pi_id=5
        
       
        
        image_data = request.POST['image_file'].file.read()
     
	 
	  
      

        current_folder = os.path.dirname(__file__)
        filename = "../static/uploaded_images/%s.jpg" % item_id
        complete_path = os.path.abspath(os.path.join(current_folder, filename))
        #print(complete_path)
        open(complete_path, 'wb').write(image_data)
        I.item_value= 'static/uploaded_images/%s.jpg' % item_id
        DBSession.add(I)
        DBSession.flush()
        request.session.flash("Image uploaded!")
        return HTTPFound(location=request.route_url('show_image',item_id=item_id))
        
   

   

    return {'project_name':project_name,'parent_item':parent_item}
  
  

@view_config(route_name='upload_f', renderer='upload_f.mako')
def upload_file(request):

    project_name = request.matchdict['pname']
    records = []
    header = False
    fields = []
    print(project_name)
    p_id = DBSession.query(Info_projects.ip_id).filter_by(name=project_name).one()
    print("ID")
    i=str(p_id[0])
    print(i)
   
    item_id=0
    for i_id in DBSession.query(project_items.pi_id).all():
      #print("item ID")
      
      item_id=i_id[0]
    print("item ID")  
   # print(str(i_id[0]))
   
    item_id =item_id+1
    print(item_id)
    dbitem_id=0
    for db_id in DBSession.query(db_itemss.db_item_id).all():
      print("dbitem ID")
      
      dbitem_id=db_id[0]
      print(dbitem_id)
    
    dbitem_id =dbitem_id+1
    List=[]
    d_order  =DBSession.query(project_items).filter_by(infoproject_id=i).all()
     
      
    for d in d_order:
      List.append((d.display_order))
      
    print("display_order********************************************") 
    #print(display_order)
    display_order=len(List)
   
      
    display_order =display_order+1
    
    if 'POST' == request.method:
        r = csv.reader(request.POST['csv_file'].file)
        file_name=(request.POST['csv_file'])
        print("file name")
        print(file_name)
        i_name = (request.POST['name'])
        
        
        
      
        
       
        I =project_items()
        I.item_name=i_name
        I.parent_item='None'
        I.item_type='DbItem'
       
        I.display_order=display_order
        
        I.infoproject_id=i
        I.pi_id=item_id
       # I.item_value=item_id
        #I.item_value= 'static/uploaded_images/%i.jpg' % item_id
        DBSession.add(I)
        DBSession.flush()
        print("p id ")
        print(I.pi_id)
        print("rowwwwwwwwwwwwwwwwwwwww")
        print(r)
          
        for row in r:
	    if not header:
	        header= row
	        fields=header
	        continue
	    records.append(row)    
        i=0
        s=0
        it=[]
        print("rowwwwwwwwwww")
        print(records)
        o=len(fields)
        q=o-1
        print(q)
        for f in fields:
          D = db_itemss()
          D.field_name=f
          D.projectitem_id=item_id
          DBSession.add(D)
          DBSession.flush()
          print("db item id")
          print(D.db_item_id)
          it.append(D.db_item_id)
        rec_id = 0  
        for o in records:
         rec_id += 1
         for i in range(len(fields)):
	   k=db_recordss()
	   k.db_rec_id = rec_id
	   k.dbitem_id = it[i]
	   k.db_item_value=o[i]
	   DBSession.add(k)
	   DBSession.flush()
	request.session.flash("File uploaded successfully!")
	return HTTPFound(location=request.route_url('show_dbitem',item_id=item_id))
	
    return {'project_name':project_name}
  

def del_dbrec(dbid):
   index=0
   
   for db_rec in DBSession.query(db_recordss).filter_by(dbitem_id=db_id[index]).all():
     DBSession.delete(db_rec)
  
     DBSession.flush()
     index +=1










@view_config(route_name='del_item')
def delete(request):
  
 i_id = request.matchdict['item_id']
 print(i_id)
 I = DBSession.query(project_items).filter_by(pi_id=i_id).first()
 print("type")
 #print(I.item_type)
 
 

 if(I.item_type=='DbItem'):
   print("data")
   iid=DBSession.query(db_itemss.db_item_id).filter_by(projectitem_id=I.pi_id).all()
   db_id=[]
   for h in iid:
     j=str(h[0])
     db_id.append(j)
     
    
   index=0
   print("**")
   #print(db_id[index])
   for i in db_id:
      for db_rec in DBSession.query(db_recordss).filter_by(dbitem_id=i).all():
        print("data")
        print(db_rec)
     #print(db_rec.db_rec_id)
     #print(db_rec.dbitem_id)
     #print(db_rec.db_item_value)
        DBSession.delete(db_rec)
        DBSession.flush()
   for iid in DBSession.query(db_itemss).filter_by(projectitem_id=I.pi_id).all():
        DBSession.delete(iid)
     
  
        DBSession.flush()
  
   DBSession.delete(I)
     
  
   DBSession.flush() 
 elif(I.item_type=='Image'):
  
   
   current_folder = os.path.dirname(__file__)
   filename = "../static/uploaded_images/%s.jpg" % i_id
   complete_path = os.path.abspath(os.path.join(current_folder, filename))  
   
   
   os.remove(complete_path)
   DBSession.delete(I)
   DBSession.flush()
   
 elif(I.item_type=='Email'):
   DBSession.delete(I)
   DBSession.flush()
 

  
   
 request.session.flash("Product Deleted Successfully!")
 return HTTPFound(location=request.route_url('home'))

@view_config(route_name='edit_dbitem', renderer="edit_dbitem.mako")
def edit_dbitem(request):
  
   ll=[]
   b=[]
   k=[]
   v1=[]
   v2=[]
   v3=[]
   i_id= request.matchdict['item_id']
   d_id = request.matchdict['dbitem_id']
   rec_id = request.matchdict['rec_id']
   
   
   for iid in DBSession.query(db_itemss).filter_by(projectitem_id=i_id).all():
    
     ll.append(int(iid.db_item_id))
     
   
   for l in ll:
     v={}
     values=DBSession.query(db_recordss).filter_by(db_rec_id=rec_id).filter_by(dbitem_id=l).first()
     v['value']=(str(values.db_item_value))
     v['rid']=(int(values.db_rec_id))
     v['did']=(int(values.dbitem_id))
     
  
     b.append(v)
     
    #print("+++++") 
   #print(b)
   
   
   k1=[]
   k2=[]
   k3=[]
   if "POST"==request.method:
     
     for v in b:
       k1.append(request.POST[v['value']])
     
     o=0
     for l in ll:
       values=DBSession.query(db_recordss).filter_by(db_rec_id=rec_id).filter_by(dbitem_id=l).first()
       values.db_item_value=k1[o]
       o=o+1
       DBSession.flush()
     
     
       
       
       
     #did=(request.POST['d_id'])
     #rid=(request.POST['r_id'])
   print("*******")
   print(k)
     
     
     #values.db_item_value=v
     #DBSession.flush()
     
   
   return{'rec_id':rec_id,'dbitem_id':d_id,'rec_value':b,'item_id':i_id,'ll':ll}
   

@view_config(route_name='show_item', renderer="show_item.mako")
def show_item(request):
 i_id = request.matchdict['item_id']

 print(i_id)
 p_id=DBSession.query(project_items.infoproject_id).filter_by(pi_id=i_id).first()
 p_name=DBSession.query(Info_projects.name).filter_by(ip_id=int(p_id[0])).first()
 pname=(str(p_name[0]))
 item_data=DBSession.query(project_items).filter_by(pi_id=i_id).all()
 i_type=DBSession.query(project_items.item_type).filter_by(pi_id=i_id).first()
 print("item type")
 print((str(i_type[0])))
 p_id=DBSession.query(project_items.parent_item).filter_by(pi_id=i_id).first()
 parent_id=str(p_id[0])
 print("parend iddddddddddddddddd")
 print(parent_id)
 l=[]
 
  
 #child_items=[]  
 #contact=DBSession.query(project_items).filter_by(pi_id=parent_id).all()
 #for data in contact:
  # d={}
   #d['name']=data.item_name
   #d['value']=''
   #child_items.append(d)
 #for child in DBSession.query(project_items).filter_by(parent_item=parent_id).all():
       
  #print("PPPPPPPPPPPPPPPPPPPPP")
  #print(child.item_name)
  #if(child.item_name!=""):
   # d={}
    #d['name']=str(child.item_name)
    #d['value']=int(child.item_value)
    #child_items.append(d)
  
    #return{'item_data':item_data,'pname':pname,'item_type':str(i_type[0]),'child':child_items,'item_id':i_id}
  #print(child_items)  
    
 
       
 
 
 
 return{'item_data':item_data,'pname':pname,'item_type':str(i_type[0])}
 
 
 
 
@view_config(route_name='show_image', renderer="show_image.mako")
def show_image(request):
 i_id = request.matchdict['item_id']
 print(i_id)
 p_id=DBSession.query(project_items.infoproject_id).filter_by(pi_id=i_id).first()
 p_name=DBSession.query(Info_projects.name).filter_by(ip_id=int(p_id[0])).first()
 I = DBSession.query(project_items).filter_by(pi_id=i_id).all()
 current_folder = os.path.dirname(__file__)
 filename = "../static/uploaded_images/%s.jpg" % i_id
 complete_path = os.path.abspath(os.path.join(current_folder, filename))
 print("project name")
 print(str(p_name[0]))
 pname=(str(p_name[0]))

   
   
  
   
 #print(I.item_type)
 #if(I.item_type=='Image'):
   
 return{'path':filename,'pname':pname}
 
@view_config(route_name='edit_item' , renderer='edit_item.mako')
def edit_item(request):
  
 i_id = request.matchdict['item_id']
 print(i_id)
 I = DBSession.query(project_items).filter_by(pi_id=i_id).first()
 print("type")
 print(I.item_type)
 
 

 
 

 if(I.item_type=='Image'):
    if "POST" == request.method:
        i_name = (request.POST['name'])
        
        
        p_item = int(request.POST['p_item'])
        d_order = int(request.POST['d_order'])
        image_data=[]
        image_data = request.POST['image'].file.read()
        current_folder = os.path.dirname(__file__)
        filename = "../static/uploaded_images/%s.jpg" % i_id
        complete_path = os.path.abspath(os.path.join(current_folder, filename))
        #print(complete_path)
        open(complete_path, 'wb').write(image_data)
        I.item_value= 'static/uploaded_images/%s.jpg' % i_id
        
        
      
        I.item_name=i_name
        I.display_order=d_order
        I.parent_item=p_item
        
        
        DBSession.flush()
        request.session.flash("Image uploaded!") 
    return{'item_id':i_id,'type':'image','data':I} 
 
 
 
 
 elif(I.item_type=='Email'):
   e = EmailForm(request.POST, I)
   if "POST" == request.method and e.validate():
   
      
      
      
        
        e.populate_obj(I)
        
        DBSession.flush()
        request.session.flash("(:")
    
    
    
   return{'email_form':e,'item_id':i_id,'type':'email'} 
 
 elif(I.item_type=='DbItem'):
   i_id = request.matchdict['item_id']
   print(i_id)
   f_name=[]
   f_type=[]
 
   listt=[]
 
 for data in DBSession.query(db_itemss).filter_by(projectitem_id=i_id).all():
    var1=str(data.field_name)
    f_name.append(var1)
    var2=str(data.field_type)
    f_type.append(var2)
    print(f_name)
    print(f_type)
 iid = DBSession.query(db_itemss.db_item_id).filter_by(projectitem_id=i_id).all()
 ll=[]
 for h in iid:
   j=str(h[0])
   ll.append(j)
   print("ll")
   print(ll)
   
 d={}
 
 f_value=[]
 rec_id=[]
 dbid=[]
 row=[]
 pp=[]
 o=0
 listt=[]
 for l in ll: 
   d2=[]
   for data in DBSession.query(db_recordss).filter_by(dbitem_id=l).all():
     d={}
     
     print(ll[o])
     row=[]
     var4=str(data.db_rec_id)
     var5=str(data.dbitem_id)
     var3=str(data.db_item_value)
     d['d_id']=var4
     d['dbitem_id']=var5
     d['db_rec']=var3
     row.append(var4)
     row.append(var5)
     row.append(var3)
     d2.append(var4)
 
     listt.append(d)
     #break
     #o=o+1
     
     #print(listt)
 
 oreder=sorted(listt)  
 print(oreder)
 print("iiiiiiiiiiiiiiiii")
 #print(d2)
 
   
   
 return{'f_name':f_name,'f_value':oreder,'type':'dbitem','item_id':i_id,'index':d2}
   
 
 
 
 return{'item_id':i_id}
    

  

@view_config(route_name='inputs/new', renderer='new_input.mako')
def add_input(request):  
   
    inputt = AddInputForm(request.POST)
    p_name= request.matchdict['item_id']
    p_id=DBSession.query(Info_projects.ip_id).filter_by(name=p_name).first()
    
    
    
    
    
    
    if "POST" == request.method and inputt.validate():
      
      
      I =user_input()
      
      I.project_id=(int(p_id[0]))
      
      
      
      inputt.populate_obj(I)
      DBSession.add(I)
      DBSession.flush()
      print("idddddddddddddddddd")
      input_id=(I.input_id)
      #request.session.flash("Added")
      return HTTPFound(location=request.route_url('inputs/manage',item_id=p_name,input_id=input_id))	     
	     
      
      
      
        
        
       
        
        
    return {'item_id':p_name,'add_input':inputt}
  
  
@view_config(route_name='inputs/delete' ,renderer='input_manage.mako')
def input_delete(request):
  if_id = request.matchdict['if_id']
  pname=request.matchdict['pname']
  row=DBSession.query(input_fields).filter_by(if_id=if_id).first()
  data=DBSession.query(input_fields).filter_by(if_id=if_id).all()
  for values in data:
    user_input_id=int(values.user_input_id )
  
 
  
  
    
    
  DBSession.delete(row)
  DBSession.flush()
  request.session.flash("Input Field Deleted successfully")
  return HTTPFound(location=request.route_url('inputs/manage',item_id=pname,input_id=user_input_id))
 
      
      
  
    
  
  
  
@view_config(route_name='inputs/manage', renderer='input_manage.mako')
def manage(request):
  print("idddddddddddddddddddddddddddddddddddddddddd")
  
  input_id = request.matchdict['input_id']
  p_name= request.matchdict['item_id']
  section_item_id=[]
  p_items=[]
  d_items=[]
  p_id=DBSession.query(Info_projects.ip_id).filter_by(name=p_name).first()
  for section_item in DBSession.query(project_items).filter_by(infoproject_id=int(p_id[0])).all():
    print(section_item.item_type)
    if(('DbItem'==section_item.item_type)|('Section'==section_item.item_type)):
       
       section_item_id.append(int(section_item.pi_id))
  print("sectionnnnnnnnn id")
  print(section_item_id) 
  for id in section_item_id:
    for p_item in DBSession.query(project_items).filter_by(parent_item=id).all():
      name=DBSession.query(project_items.item_name).filter_by(pi_id=id).first()
      d={}
      c_name=str(name[0])+"  --->  "+str(p_item.item_name)
      c_id="pi_"+str(p_item.pi_id)
      d['name']=c_name
      d['id']=c_id
      p_items.append(d)
  print("p itemsssssssssssssssssssss")
  print(p_items)
  for id in section_item_id:
    for p_item in DBSession.query(db_itemss).filter_by( projectitem_id=id).all():
      name=DBSession.query(project_items.item_name).filter_by(pi_id=id).first()
      d={}
      c_name=str(name[0])+"  --->  "+str(p_item.field_name)
      c_id="db_"+str(p_item.db_item_id)
      d['name']=c_name
      d['id']=c_id
      p_items.append(d)
  print("d itemsssssssssssssssssssss")
  print(d_items)
  list=[]
  list.append(p_items)
  list.append(d_items)
  data=[]
  for fields in DBSession.query(input_fields).filter_by(user_input_id=input_id).all():
      d={}
      d['name']=str(fields.if_name)
      d['if_id']=int(fields.if_id)
      d['type']=str(fields.if_type)
      d['input_field_id']=str(fields.input_field_id)
      data.append(d)
    #print(data)
  if "POST"==request.method:
    id=0
    for i_id in DBSession.query(input_fields.if_id).all():
      #print("item ID")
      
      id=i_id[0]
    print("item ID")  
   # print(str(i_id[0]))
   
    id =id+1
    input_id = request.matchdict['input_id']
    type=str(request.POST['type'])
    f_id=str(request.POST['field'])
    name=str(request.POST['field_name'])
    #request.session.flash(type)
    #request.session.flash(name)
    #request.session.flash(f_id)
    #request.session.flash(id)
    
    I=input_fields()
    I.if_id=id
    I.if_name=name
    I.user_input_id=input_id
    I.if_type=type
    I.input_field_id=f_id
    DBSession.add(I)
    DBSession.flush()
    request.session.flash(I.user_input_id)
    
      
      
    return{'dataa':data,'list':p_items,'input_id':input_id,'pname':p_name}
    
    
    
   
    
  
      
    
  
  return{'list':p_items,'input_id':input_id,'pname':p_name,'dataa':data}
  
  
    
    
    
   
    
  
    
   
    
    
    
  
  
@view_config(route_name='show_input',renderer='input_display.mako')
def show_input(request): 
  p_id = request.matchdict['p_id']
  input_id = request.matchdict['input_id']
  print("piddddddddddddddddddd")
  print(input_id)
  input_id=[]
  values=[]
  var=DBSession.query(user_input).filter_by(project_id=p_id).all()
  for v in var:
    a=int(v.input_id)
    input_id.append(a)
    
  print("+++++++++++++++++++++++")
  print(input_id)
  for i in input_id:
    for data in DBSession.query(input_fields).filter_by(user_input_id=i):
      d={}
      d['name']=str(data.if_name)
      d['type']=str(data.if_type)
      d['id']=i
      d['ifi']=int(data.if_id)
      values.append(d)
  print("data")
  print(values)
  
  return{'values':values,'p_id':p_id,'input_id':input_id}
      
      

    



@view_config(route_name='email', renderer='email.mako')
def add_email(request):
    email_form = EmailForm(request.POST)
    project_name = request.matchdict['pname']
    item_id=1
    
    
    print(project_name)
    p_id = DBSession.query(Info_projects.ip_id).filter_by(name=project_name).one()
    print("ID")
    i=str(p_id[0])
    print(i)
    List=[]
    d_order =DBSession.query(project_items).filter_by(infoproject_id=i).filter_by(parent_item='None').all()
     
      
    for d in d_order:
      if(d.parent_item=='None'):
        List.append((d.item_name))
      
    print("display_order********************************************") 
    #print(display_order)
    display_order=len(List)
   
    print(List)  
    display_order =display_order+1
    print(display_order)
    parent_item=[]
    for sec in DBSession.query(project_items).filter_by(item_type='section').filter_by(infoproject_id=i).all():
      d={}
      d['sec_name']=str(sec.item_name)
      d['sec_id']=int(sec.pi_id)
      
      parent_item.append(d)
      
    print("llllllllllllllllllllllllllllllllllllllllllll")
    print(parent_item)
    for i_id in DBSession.query(project_items.pi_id).all():
      #print("item ID")
      
      item_id=i_id[0]
    print("item ID")  
   # print(str(i_id[0]))
   
    item_id =item_id+1  
      
      
    
    
    print("oooooooooooooooooooooooooooo")
  
    if "POST" == request.method and email_form.validate():
      
        
        if(parent_item)==[]:
	  
	   I =project_items()
	   
	   I.item_type='Email'
       
           I.display_order=display_order
           I.parent_item='None'
           I.infoproject_id=i
           I.pi_id=item_id
           
           p_item='None'
          
        else:
	   
	   
           I =project_items()
           p_item = str(request.POST['p_item'])
           print("ttttttttttttttttttttttttttttt")
	   print(p_item)
           if(p_item=='0'):
	     I.parent_item='None'
	     I.item_type='Email'
             I.parent_item=p_item
             I.pi_id=item_id
             I.display_order=display_order
             I.infoproject_id=i
           else:
           
         
             l=[]
             d=DBSession.query(project_items).filter_by(infoproject_id=i).filter_by(parent_item=p_item).all()
             for dd in d:
	       l.append(dd.display_order)
	     display_order=len(l)
	     display_order=display_order+1
	       
             I.display_order=display_order
           
             I.infoproject_id=i
	     
	     
             I.item_type='Email'
             I.parent_item=p_item
             I.pi_id=item_id
           
       
           
           
             I.infoproject_id=i
           
        
        print("p id ")
        print(I.pi_id)
        #I.pi_id=5
     
      
      
      
        email_form.populate_obj(I)
        DBSession.add(I)
        DBSession.flush()
        request.session.flash("Email item added Successfully !!")
        return HTTPFound(location=request.route_url('show_item',item_id=item_id))
      
      
        
    
    
      
      
        
        
       
        
        
    return {'project_name':project_name,'add_email':email_form,'parent_item':parent_item}
  
  
  
@view_config(route_name='del_dbitem', renderer="del_dbitem.mako") 
def del_dbitem(request):
 i_id = request.matchdict['item_id']
 print(i_id)
 f_name=[]
 f_type=[]
 
 listt=[]
 listt1=[]
 listt2=[]
 
 for data in DBSession.query(db_itemss).filter_by(projectitem_id=i_id).all():
    var1=str(data.field_name)
    f_name.append(var1)
    var2=str(data.field_type)
    f_type.append(var2)
    print(f_name)
    print(f_type)
 iid = DBSession.query(db_itemss.db_item_id).filter_by(projectitem_id=i_id).all()
 ll=[]
 
 for h in iid:
   j=str(h[0])
   ll.append(j)
   print("ll")
   print(ll)
 mm=[1,2]
 pp=[]
 kk=[]
 for l in ll:
    pp=DBSession.query(db_recordss.db_rec_id).filter_by(dbitem_id=l).all()
 print("PPPPPPPPPPPPPP")
 print(str(pp))
 for h in pp:
   j=str(h[0])
   kk.append(j)
 for m in kk:
   
   f_value=[]
   rec_id=[]
   dbid=[]
   row=[]
   o=[]
   
   q=[]
   for l in ll:
    for data in DBSession.query(db_recordss).filter_by(dbitem_id=l).filter_by(db_rec_id=m).all():
     print(l)
     
     d={}
     p=[]
     var3=str(data.db_item_value)
     #var4=str(data.db_rec_id)
     #var5=str(data.dbitem_id)
     var4=str(data.db_rec_id)
     var5=str(data.dbitem_id)
     var3=str(data.db_item_value)
     d['rec_id']=var4
     #d['dbitem_id']=var5
     #d['db_rec']=var3
     #row.append(var4)
     #row.append(var5)
     o.append(var3)
     p.append(var4)
     q.append(var4)
   listt.append(o)
   listt1.append(q)
   listt2.append(q)
   
     
 #for v in listt:
   
 print("********")    
 print(listt) 
 print("_______________________-")    
 print(listt1)
   
     
 
 #print(listt)
 
 p=[]
 
  
 print(p)
 v=1
 if "POST"==request.method:
     
     for o in request.POST[mm]:
      print("++++++++++++++++++")
      print(o)
     
     
   
 return{'f_name':f_name,'f_value':listt,'idz':kk,'item_id':i_id}
 
@view_config(route_name='del_rec')
def del_rec(request):
  i_id=request.matchdict['item_id']
  rec_id=request.matchdict['rec_id']
  print(rec_id)
  print(i_id)
  ll=[]
  values=[]
  rid=[]
  did=[]
  oo=[]
  b=[]
  for iid in DBSession.query(db_itemss).filter_by(projectitem_id=i_id).all():
    
     ll.append(int(iid.db_item_id))
     
  print(ll) 
  for l in ll:
     v={}
     values=DBSession.query(db_recordss).filter_by(db_rec_id=rec_id).filter_by(dbitem_id=l).first()
    
     DBSession.delete(values)
    
     DBSession.flush()
     
    
     
     
  
     
  
     
     
     
  
  request.session.flash("Record Deleted ")
  return HTTPFound(location=request.route_url('del_dbitem', item_id=i_id))
  
  

@view_config(route_name='show_dbitem', renderer="show_dbitem.mako")
def show_dbitem(request):
 i_id = request.matchdict['item_id']
 p_id=DBSession.query(project_items.infoproject_id).filter_by(pi_id=i_id).first()
 p_name=DBSession.query(Info_projects.name).filter_by(ip_id=int(p_id[0])).first()
 print(i_id)
 f_name=[]
 f_type=[]
 
 listt=[]
 
 for data in DBSession.query(db_itemss).filter_by(projectitem_id=i_id).all():
    var1=str(data.field_name)
    f_name.append(var1)
    var2=str(data.field_type)
    f_type.append(var2)
    print(f_name)
    print(f_type)
 iid = DBSession.query(db_itemss.db_item_id).filter_by(projectitem_id=i_id).all()
 ll=[]
 
 for h in iid:
   j=str(h[0])
   ll.append(j)
   print("ll")
   print(ll)
 mm=[1,2]
 pp=[]
 kk=[]
 for l in ll:
    pp=DBSession.query(db_recordss.db_rec_id).filter_by(dbitem_id=l).all()
 print("PPPPPPPPPPPPPP")
 print(str(pp))
 for h in pp:
   j=str(h[0])
   kk.append(j)
 for m in kk:
   
   f_value=[]
   rec_id=[]
   dbid=[]
   row=[]
   o=[]
   for l in ll:
    for data in DBSession.query(db_recordss).filter_by(dbitem_id=l).filter_by(db_rec_id=m).all():
     print(l)
     
     d={}
     
     var3=str(data.db_item_value)
     #var4=str(data.db_rec_id)
     #var5=str(data.dbitem_id)
     var4=str(data.db_rec_id)
     var5=str(data.dbitem_id)
     var3=str(data.db_item_value)
     #d['rec_id']=var4
     #d['dbitem_id']=var5
     d['db_rec']=var3
     #row.append(var4)
     #row.append(var5)
     o.append(var3)
   listt.append(o)
   
     
 #for v in listt:
   
 print("********")    
 print(listt)    
   
     
 
 #print(listt)
 
 p=[]
 
  
 print(p)
 return{'f_name':f_name,'f_value':listt,'pname':str(p_name[0])}
 



   

@view_config(route_name='field_type', renderer="field_type.mako")   
def my_pro(request): 
    
        i_id = request.matchdict['item_id']
        fields=[]
        c=[]
        f_form=FieldForm(request.POST)
        print(f_form.fieldd_type.choices)
        print("*****************")
	
        iid = DBSession.query(db_itemss.db_item_id).filter_by(projectitem_id=i_id).all()
        ll=[]
        for h in iid:
	  j=str(h[0])
	  ll.append(j)
        print("ll")
        print(ll)
        
      
      
       
        if 'POST' == request.method :
	  
	    l=[]
	    field_types=[]
	    kk=[]
	    
	    f= f_form.fieldd_type.data
	    for u in fields:
	      uu=request.POST[u]
	      kk.append(uu)
	    print("ghfhfhdfhtytydt")
	    print(fields)
	      
	    for l in ll:
	      ff = request.POST[l]
	      field_types.append(ff)
	    
	    fff=[]
	    for f in field_types:
	      j=str(f)
	      fff.append(j)
            s=len(fff)  
            index=0  
            for table_column in DBSession.query(db_itemss).filter_by(projectitem_id=i_id).all():
	         
		  
		   table_column.field_type = fff[index]
		   
		   DBSession.flush()
		   index +=1
           
            f_name=[]
            f_type=[]
            
            for data in DBSession.query(db_itemss).filter_by(projectitem_id=i_id).all():
	      var1=str(data.field_name)
	      f_name.append(var1)
	      var2=str(data.field_type)
	      f_type.append(var2)
	    print(f_name)
	    print(f_type)
	    for l in ll:
	      for data in DBSession.query(db_recordss).filter_by(dbitem_id=l).all():
		print(l)
		print(data.db_item_value) 
		
	    p_id= DBSession.query(project_items.infoproject_id).filter_by(pi_id=i_id).first()
	    name=DBSession.query(Info_projects.name).filter_by(ip_id=int(p_id[0])).first()
	
	    request.session.flash("Field types edited successfully !! ")
	    
            return HTTPFound(location=request.route_url('view_items',pname=str(name[0])))
       

	   
	
        db_fields = DBSession.query(db_itemss.field_name).filter_by(projectitem_id=i_id).all()
        c=(db_fields)
       
        for cc in c :
	  fields.append(str(cc[0]))
	#for n in fields:
	 # f_form.field_name.data.append(n)
        print(":::")
        #print(fields)
        print("PP")
        print(fields)
        print(len(fields))

        #project_item = DBSession.query(db_itemss).filter_by(field_name,projectitem_id=item_id).all()
        
    #print(f_form)
        
        #print(f_form.fieldd_type)
       
	   
	
	  #for i in request.POST('dd'):
	    #strikes = (request.POST('dd'))
	  # for x in request.POST(str('dd')):
	   
	    
	   
	  
	   
	  
	#  image_data = request.POST['image_file'].file.read()
         # project_item = DBSession.query(project_items).filter_by(pi_id=item_id).first()
       # if not project_item:
        #    return HTTPNotFound(message="Project item does not exist")

        
    
        #f_form.field_type.choices = types
       
	 
	  

        
        #P = Product()
           
        #product_form.populate_obj(P)
        #DBSession.add(P)
    
        #if "POST" == request.method and f_form.validate():
	 # for t in f_form.field_type.choices:
	  #print(t)
        
        #return HTTPFound(location=request.route_url('home'))
    #project_name = request.matchdict['pname']
    #P = DBSession.query(Info_projects).filter_by(name=project_name).first()
    #if not P:
     # 
    #image_items = DBSession.query(project_items).filter_by(infoproject_id=P.ip_id).order_by(project_items.display_order)
       
       
	    
        
	    
	tt=['cell','image','text']  
        return {  'fields':fields,'f_form':f_form,'ll':ll,'tt':tt,'item_id':i_id}
    #P = DBSession.query(Info_projects).filter_by(name=project_name).first()
    #if not P:
     #   return HTTPNotFound(message="Project %s does not exist" % project_name)
 
    #return{'f_form':f_form}

@view_config(route_name='field_save')
def ff(request):

   if "POST" == request.method and f_form.validate():
     request.session.flash("Image uploaded!")
   
@view_config(route_name='primary_display' , renderer='primary_display.mako')
def primary_display(request):
 v=[]
 i_id = request.matchdict['item_id']
 print("********************")
 print(i_id)
 I = DBSession.query(project_items).filter_by(pi_id=i_id).first()
 for data in DBSession.query(db_itemss).filter_by(projectitem_id=i_id).all():
   print(data.field_name)
   d={}
   
   d['field_name']=str(data.field_name)
   d['db_id']=int(data.db_item_id)
   v.append(d)
 print("____________________________")
 print(v)
 for i in v:
  print(i)
 pp=[]
 #for u in v:
   #print(u['db_id'])
 b=[1,2,3]
 if "POST" == request.method:
         import cgi
         form = cgi.FieldStorage()

# getlist() returns a list containing the
# values of the fields with the given name
         
         
         a=(request.POST['primary_display'])
          
         
         D= DBSession.query(db_itemss).filter_by(db_item_id=a).first()
         D.primary_display_field=True
         DBSession.flush()
         print("++++++++++++++++++")
         print(a)
          
    
   
   
     
   
   
 return{'item_id':i_id,'data':v}
 
 
 
   
   
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
#@view_config(route_name='show_f', renderer='show_f.mako')

  
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
