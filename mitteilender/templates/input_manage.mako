<%inherit file="base.mako"/>

<<<<<<< HEAD
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


 
=======


>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b




<<<<<<< HEAD
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
=======









<form action="${request.route_url('input_manage',item_id=item_id,input_id=input_id)}" method="POST">


Input Name:
<input type="text" value=${input_name} >
<br /><br /><br />
<select name=fields>
%for data in range(len(db_item)) :
%for id in range(len(db_id)):
%if (data==id):



 <option  value=${db_id[id]} name=${db_id[id]}>${db_item[data]}</option>

  %endif

%endfor
%endfor

<select>
<br /><br /><br />
 <input type="radio" name=type value="open"> Open
<br /><br /><br />
 <input type="radio" name=type value="multi_select"> Multi Select
<br /><br /><br />
 <input type="radio" name=type value="single_select"> Single Select
<br /><br /><br />
 
  
     
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
  <input type="submit" name="form.submitted" value="Add " />
</form>

</div>