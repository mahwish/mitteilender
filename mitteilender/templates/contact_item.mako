<%inherit file="base.mako"/>
<%inherit file="home.mako"/>

<%inherit file="base.mako"/>
  <h1>Add Contact Item: ${project_name}</h1>
<div>
   
                    <form action="${request.route_url('contact_item', pname=project_name)}" method="POST" >
                                <br /><br /><br /> 
                  Contact Item<input type="text" name="contact_name" value=""  /><br /><br /><br />
                  
                  
                  
                  
                      <h1>      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp      &nbsp&nbsp&nbsp&nbspLanline </h1>
                   Name: <input type="text" name="l_name" value=""  /><br /><br /><br />
                     Number: <input type="text" name="l_num" value=""  /><br /><br /><br />
                     
                     
                     <h1> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp      &nbsp&nbsp&nbsp&nbspCell </h1>
                       Name: <input type="text" name="c_name" value=""  /><br /><br /><br />
                     
                         Number<input type="text" name="c_num" value=""  size="15" required /><br /><br /><br />
   

 
  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp      &nbsp&nbsp&nbsp&nbsp <input type="submit" name="form.submitted" value="Add" />



      

        
                     
                  
                      
                        
                        
                       

</form>

<br /><br /><br /><br /><br /><br />
</div> 
