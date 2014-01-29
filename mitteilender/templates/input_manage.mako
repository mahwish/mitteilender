<%inherit file="base.mako"/>

<table>

        <tr class="tr_heading">
        
            <th>ID</th>
            <th>Name</th>
            
            <th>Type</th>
              </tr>
        
       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
       %for d in dataa:
       
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td>${d['if_id']}</td>
                <td>${d['name']}</td>
               
                <td>${d['type']}</td>
                  
               <td>    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('inputs/delete',pname=pname,if_id=d['if_id'])}"><font color="teal"><b>Delete</a></td>
                </tr>
                
      %endfor
      </table>


 




<form action="${request.route_url('inputs/manage',item_id=pname,input_id=input_id)}" method="POST">



 <br /><br /><br />

&nbsp&nbsp&nbsp&nbsp&nbsp&nbspInput Name:
 <input type="text" name=field_name required />
     <br /><br /><br />
<br /><br /><br />
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<select name=field>
%for data in list :



 <option  value=${data['id']} name=${data['id']}>${data['name']}</option>

 
%endfor
<option name=${data['id']}  value='No Field' >No Field</option> 
<select>
   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
<select name=type>
<option  value="open" name="open" >Open</option>

<option  value="single_select" name="single_select"> Single Select</option>

<option  value="multi_select" name="multi_select">Multi Select</option>
</select>
 
  
    <br /><br /><br /><br /><br /><br />  
  <input type="submit" name="form.submitted" value="Add " />
</form>

</div>