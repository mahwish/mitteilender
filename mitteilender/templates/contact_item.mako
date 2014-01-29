<<<<<<< HEAD
<!DOCTYPE html>
<html>
<head>
<script>
function validateForm(p)
{
var numbers = /^[-+]?[0-9]+$/;  
var namepattern=/^[a-zA-Z]+$/;
var cellpattern = /^\d{11}$/
var landlinepattern = /^\d{10}$/
 if (p['contact_name'].value=="")
 {
  
  document.getElementById('c_name').innerHTML="Please enter name.";
  
  return false;
 }
  if (!namepattern.test(p['contact_name'].value))
 {
  
  document.getElementById('c_name').innerHTML="Please enter only alphabets.";
  
  return false;
 }

  if ((p['cell_name'].value=="")&&(p['landline_name'].value==""))
 {
  
  document.getElementById('cell_name').innerHTML="Please enter name.";
  document.getElementById('landline_name').innerHTML="Please enter name.";
  
  return false;
 }
 if (!namepattern.test(p['cell_name'].value)&&(!namepattern.test(p['landline_name'].value)))
 {
  
  document.getElementById('cell_name').innerHTML="Please enter only alphabets.";
   document.getElementById('landline_name').innerHTML="Please enter only alphabets.";
  
  return false;
 }
 
   
 
if ((p['cell_name'].value.length>20)&&(p['landline_name'].value.length>20))
 {
  
  document.getElementById('cell_name').innerHTML="Please enter less than 20 characters.";
    document.getElementById('landline_name').innerHTML="Please enter less than 20 characters.";
  
  
  return false;
 } 
if ((p['cell_number'].value=="")&&(p['landline_number'].value==""))
 {
  
  document.getElementById('cell_num').innerHTML="Please enter number.";
    document.getElementById('landline_num').innerHTML="Please enter number.";
  
  return false;
 } 
if (isNaN(p['cell_number'].value=="")&&(isNaN(p['landline_number'].value=="")))
 {
  
  document.getElementById('cell_num').innerHTML="Please enter only digits.";
    document.getElementById('landline_num').innerHTML="Please enter only digits.";
  
  return false;
 } 
 if (isNaN(p['cell_number'].value=="")&&(isNaN(p['landline_number'].value=="")))
 {
  
  document.getElementById('cell_num').innerHTML="Please enter only digits.";
    document.getElementById('landline_num').innerHTML="Please enter only digits.";
  
  
  return false;
 } 
 if (!cellpattern.test(p['cell_number'].value)&&(!landlinepattern.test(p['landline_number'].value)))
 {
  
  document.getElementById('cell_num').innerHTML="Please enter valid number.";
  document.getElementById('landline_num').innerHTML="Please enter valid number.";
  
  return false;
 } 
if ((p['cell_number'].value.length!=11)&&(p['landline_number'].value.length!=10))
 {
  
  document.getElementById('cell_num').innerHTML="Please enter valid digits (11 for cell number).";
  document.getElementById('landline_num').innerHTML="Please enter valid digits (10 for landline number).";
  
  return false;
 }
 if ((p['cell_number'].value=="")&& (p['landline_number'].value==""))
  {
    document.getElementById('null').innerHTML="Please enter the any number.";
   
  return false;
  }
}



      

 </script>       
            
            </head>
            <body>
=======
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
<%inherit file="base.mako"/>
<%inherit file="home.mako"/>

<%inherit file="base.mako"/>
  <h1>Add Contact Item: ${project_name}</h1>
<div>
   
<<<<<<< HEAD
                    <form name="p" action="${request.route_url('add_project_item', pname=project_name,item_type='Contact')}" method="POST" onsubmit="return validateForm(p)" >
                                <br /><br /><br /> 
                                <table>
                               <tr> <td> <h3> Contact Item</h3></td></tr>
                                
<tr><td><input type="text" name="contact_name" /></td> <td> <i style="color:red;" id="c_name"></i></td></tr> 
                  <tr><td><br><br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<i style="color:red;" id="null"></i></td></tr>
                     <tr> <td> <h3> Cell Number</h3></td></tr>
                 <tr><td><label>   Name </label></td><td>
                 <input type="text" name="cell_name" value="" /></td>
                 <td> <i style="color:red;" id="cell_name"></i></td></tr>
               
          <tr><td><label>        Number</label></td><td><input type="text" name="cell_number" value="" minsize=11  /></td>
          <td> <i style="color:red;" id="cell_num"></i></td></tr></tr>
                      <tr> <td> <h3> Landline Number</h3></td></tr>
           <tr><td><label>       Name</label></td><td> <input type="text" name="landline_name" value="" />
                <td>   <i style="color:red;" id="landline_name"></i></td></tr>
              <tr><td><label>     Number</label></td><td><input type="text" name="landline_number" value=""  minsize=10 />
           </td><td> <i style="color:red;" id="landline_num"></i></td></tr></tr>
           
           </table>
                 
=======
                    <form action="${request.route_url('contact_item', pname=project_name)}" method="POST" >
                                <br /><br /><br /> 
                  Contact Item<input type="text" name="contact_name" value=""  /><br /><br /><br />
                  
                  
                  
                  
                      <h1>      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp      &nbsp&nbsp&nbsp&nbspLanline </h1>
                   Name: <input type="text" name="l_name" value=""  /><br /><br /><br />
                     Number: <input type="text" name="l_num" value=""  /><br /><br /><br />
                     
                     
                     <h1> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp      &nbsp&nbsp&nbsp&nbspCell </h1>
                       Name: <input type="text" name="c_name" value=""  /><br /><br /><br />
                     
                         Number<input type="text" name="c_num" value=""  size="15" required /><br /><br /><br />
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
   

 
  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp      &nbsp&nbsp&nbsp&nbsp <input type="submit" name="form.submitted" value="Add" />

<<<<<<< HEAD
         
=======


      

        
                     
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
                  
                      
                        
                        
                       

</form>
<<<<<<< HEAD
</body>
<br /><br /><br /><br /><br /><br />
</div> 
</html>
=======

<br /><br /><br /><br /><br /><br />
</div> 
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
