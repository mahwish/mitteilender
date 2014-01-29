<%inherit file="base.mako"/>

<div>
   <h1>Project Name : ${project_name}
  <br /><br />
Add Section Item    </h1>
    <br /><br /><br />
    
 <form action="${request.route_url('section_item',pname=project_name)}" method="POST" enctype="multipart/form-data">

<br /><br /><br />
                   Item Name: <input type="text" name="name" value=""  required/><br /><br /><br />
                  
      







      
<br /><br /><br /><br /><br /><br />
 <input type="submit"  value="Add" />
</form>

  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=project_name)}"><font color="teal"><b>Back</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp

</div>



 