<%inherit file="base.mako"/>
<%inherit file="home.mako"/>

<%def name="title()">

</%def>
      <div class="middle align-center">
        <p><font color="teal"><b>
<div>
<h1>New Text Item</h1>

<form action="${request.route_url('text_item',pname=project_name)}" method="POST">
    ${add_text.as_p() | n}
  
   
     %if (parent_item==[]):
       Parent item : 
       None
       
     
     
     %else:
      Parent item:
     <select name=p_item>




%for i in parent_item:


 <option name=${i['sec_id']} value=${i['sec_id']} >${i['sec_name']}</option>
 

 %endfor
  </select>
  %endif
</form>

<br /><br /><br /><br /><br /><br />
</div> 
  <input type="submit" name="form.submitted" value="Add" />