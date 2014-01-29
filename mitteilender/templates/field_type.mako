<%inherit file="base.mako"/>

<%def name="title()">

</%def>

<div>
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
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

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
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
>>>>>>> bcea36c4043c05d26b70fceef21c71b44940e14f
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
 


<select>
 &nbsp&nbsp&nbsp&nbsp&nbsp <input type="checkbox" name=${fields[f]}  value=${fields[f]}> 
<br /><br /><br />
 
    %endif
    %endfor
     %endfor
  <input type="submit" name="form.submitted" value="Edit " />
</form>



<<<<<<< HEAD
</div>
=======
<<<<<<< HEAD
</div>
=======
</div>
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
