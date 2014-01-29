<%inherit file="base.mako"/>

<%def name="title()">

</%def>

<div>
 <form action="${request.route_url('primary_display',item_id=item_id)}" method="POST">




      
              
         

 
%for i in data:
 <input type="radio" name=primary_display value=${i['db_id']}> ${i['field_name']}
 <br /><br /><br />
 %endfor
<br /><br /><br />

  <input type="submit" name="form.submitted" value="Edit " />
</form>



</div>



