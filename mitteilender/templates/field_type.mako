<%inherit file="base.mako"/>

<%def name="title()">

</%def>

<div>
 <form action="${request.route_url('field_type',item_id=item_id)}" method="POST">





%for l in range(len(ll)) :

%for f in range(len(fields)):
%if  l==f:

${fields[f]}




&nbsp&nbsp&nbsp&nbsp&nbsp

<select name=${ll[l]}>






 <option value="text">text</option>
  <option value="image">Image</option>
  <option value="cell">Cell</option>
  <option value="email">Email</option>

 


<select>
 &nbsp&nbsp&nbsp&nbsp&nbsp <input type="checkbox" name=${fields[f]}  value=${fields[f]}> 
<br /><br /><br />
 
    %endif
    %endfor
     %endfor
  <input type="submit" name="form.submitted" value="Edit " />
</form>



</div>