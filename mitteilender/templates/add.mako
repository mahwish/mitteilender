<%inherit file="base.mako"/>
<<<<<<< HEAD
<%inherit file="home.mako"/>
<div>
   <font color="teal" size="60px"> <font color="teal"><b> Add Project Item
=======

<div>
    <h1>Add Project Item</h1>
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
    <br /><br /><br />
    
 Please select any of the following items u want to add:

<br /><br /><br />

<a href="${request.route_url('section_item', pname=project_name)}"><font color="teal"><b>Section Item</a><br /><br /><br />                  
<a href="${request.route_url('text_item', pname=project_name)}"><font color="teal"><b>Text Item</a><br /><br /><br />
<a href="${request.route_url('contact_item', pname=project_name)}"><font color="teal"><b>Contact Item</a><br /><br /><br />
<a href="${request.route_url('email', pname=project_name)}"><font color="teal"><b>Email Item</a><br /><br /><br />
<a href="${request.route_url('upload_image', pname=project_name)}"><font color="teal"><b>Image Item</a><br /><br /><br />
<a href="${request.route_url('upload_f',pname=project_name)}"><font color="teal"><b>DB ggItem</a><br /><br /><br />




  
<br /><br /><br />
 
    
 
</form>



</div>



  
