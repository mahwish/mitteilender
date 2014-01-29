<!DOCTYPE html>
<html>
<head>
   

     
            
            </head>
            <body>
<%inherit file="base.mako"/>
<%inherit file="home.mako"/>

<%inherit file="base.mako"/>
  <h1>Add Contact Item: ${pname}</h1>
<div>
   
          
               
               
               
               %if (cname=='cell'):
               
                    <form name="p" action="${request.route_url('contact_details', pname=pname,cname=cname)}" method="POST"  >
                                <br /><br /><br /> 
                                <h1>Cell Number</h1>
                                
                 Name<input type="text" name="cell_name" required /><br /><br /><br />
                  
                     Number<input type="text" name="cell_number" required /><br /><br /><br />
                      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp      &nbsp&nbsp&nbsp&nbsp <input type="submit" name="form.submitted" value="Add" />
                       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=pname)}"><font color="teal"><b>Skip </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                      

         
                  
                      
                        
                        
                       

</form>
                     %elif (cname=='landline'):
                          <form name="p" action="${request.route_url('contact_details', pname=pname,cname=cname)}" method="POST"  >
                                <br /><br /><br /> 
                                 <h1>Landline Number</h1>
                 Name<input type="text" name="landline_name" required /><br /><br /><br />
                  
                     Number<input type="text" name="landline_number" required/><br /><br /><br />
                      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp      &nbsp&nbsp&nbsp&nbsp <input type="submit" name="form.submitted" value="Add" />
                       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=pname)}"><font color="teal"><b>Skip</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp

         
                  
                      
                        
                        
                       

</form>
%else:
                     
                 
                                <br /><br /><br /> 
                  Contact Item<input type="text" name="contact_name" value=${cname}/><br /><br /><br />
                  
                  
                  
               &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('contact_details', pname=pname,cname='cell')}"><font color="teal"><b>Cell Number</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
               &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('contact_details', pname=pname,cname='landline')}"><font color="teal"><b>Landline number</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        
                  
               
       %endif              
                  
              
                     
                    
   

 
 

      
                  
                      
                        
                        
                       


</body>
<br /><br /><br /><br /><br /><br />
</div> 
</html>