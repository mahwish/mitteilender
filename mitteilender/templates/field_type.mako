<%inherit file="base.mako"/>

<div>
<h1> Field Type</h1>
<div style="margin-left: 50px;">
<form action="${request.route_url('field_type')}" method="POST" enctype="multipart/form-data">
    
   <input type="file" name="csv_file" />
                        <input type="submit" value="upload" />
                     </form>
 <form action="${request.route_url('field_type')}" method="POST" enctype="multipart/form-data">
<br><br><br><br><br><br><br><br><input type="submit" value="done" /><br><br>
  %for f in f_form.field_name.data:
  ${f}&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  ${f_form.field_type}
  <br><br><br><br><br><br><br><br>
  %endfor
  <br><br>
  
</form>
</div>
 
 
