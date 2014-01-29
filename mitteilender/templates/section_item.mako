<%inherit file="base.mako"/>

<div>
<<<<<<< HEAD
   <h1>Project Name : ${project_name}
  <br /><br />
Add Section Item    </h1>
=======
    <h1>Add Section Item</h1>
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
    <br /><br /><br />
    
 <form action="${request.route_url('section_item',pname=project_name)}" method="POST" enctype="multipart/form-data">

<br /><br /><br />
<<<<<<< HEAD
                   Item Name: <input type="text" name="name" value=""  required/><br /><br /><br />
=======
                   Item Name: <input type="text" name="name" value=""  /><br /><br /><br />
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
                  
      







      
<br /><br /><br /><br /><br /><br />
 <input type="submit"  value="Add" />
</form>

<<<<<<< HEAD
  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=project_name)}"><font color="teal"><b>Back</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
=======

>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b

</div>



 