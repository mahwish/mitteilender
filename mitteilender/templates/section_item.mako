<%inherit file="base.mako"/>

<div>
    <h1>Add Section Item</h1>
    <br /><br /><br />
    
 <form action="${request.route_url('section_item',pname=project_name)}" method="POST" enctype="multipart/form-data">

<br /><br /><br />
                   Item Name: <input type="text" name="name" value=""  /><br /><br /><br />
                  
      







      
<br /><br /><br /><br /><br /><br />
 <input type="submit"  value="Add" />
</form>



</div>



 