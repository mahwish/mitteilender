<%inherit file="base.mako"/>

<div>
<h1> Field Type</h1>
<div style="margin-left: 50px;">
<form action="${request.route_url('field_type')}" method="POST">
    
   
  
  ${f_form.field_type.choices}	<br></br>
 %for r in f_form.field_name:
		
			${r}&nbsp&nbsp
		
		<br></br>
		%endfor
		 

    <input type="submit" value="done" />
</form>
</div>
 
 
