<%inherit file="base.mako"/>

<div>
    <h1>Add Project Item</h1>
    <br /><br /><br />
    
 Please select any of the following items u want to add:

<br /><br /><br />

<a href="${request.route_url('section_item', pname=project_name)}"><font color="teal"><b>Section Item</a><br /><br /><br />                  
<<<<<<< HEAD
<a href="${request.route_url('text_item', pname=project_name)}"><font color="teal"><b>Text Item</a><br /><br /><br />
<a href="${request.route_url('contact_item', pname=project_name)}"><font color="teal"><b>Contact Item</a><br /><br /><br />
=======
<a href="${request.route_url('section_item', pname=project_name)}"><font color="teal"><b>Text Item</a><br /><br /><br />
<a href="${request.route_url('view_items', pname=project_name)}"><font color="teal"><b>Contact Item</a><br /><br /><br />
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
<a href="${request.route_url('email', pname=project_name)}"><font color="teal"><b>Email Item</a><br /><br /><br />
<a href="${request.route_url('upload_image', pname=project_name)}"><font color="teal"><b>Image Item</a><br /><br /><br />
<a href="${request.route_url('upload_f',pname=project_name)}"><font color="teal"><b>DB ggItem</a><br /><br /><br />




  
<br /><br /><br />
 
    
 
</form>



</div>



  
