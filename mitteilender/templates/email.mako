<%inherit file="base.mako"/>
<%inherit file="home.mako"/>

<%def name="title()">

</%def>
      <div class="middle align-center">
        <p><font color="teal"><b>
<div>
 <h1>Project Name : ${project_name}
  <br /><br />
Add Email Item    </h1>

<form action="${request.route_url('email',pname=project_name)}" method="POST">
    ${add_email.as_p() | n}
  
   
     %if (parent_item==[]):
       Parent item : 
       None
       
     
     
     %else:
      Parent item:
     <select name=p_item>




%for i in parent_item:


 <option name=${i['sec_id']} value=${i['sec_id']} >${i['sec_name']}</option>

 

 %endfor
 <option name=${i['sec_id']} value='None' >None</option> 
  </select>
  %endif
  <br /><br />
   <input type="submit" name="form.submitted" value="Add Item" />
</form>
  <br /><br /><br />
                    
    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=project_name)}"><font color="teal"><b>Back</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br /><br /><br /><br /><br /><br />
</div> 
 