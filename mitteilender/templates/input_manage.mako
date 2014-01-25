<%inherit file="base.mako"/>
















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
 
  
     
  <input type="submit" name="form.submitted" value="Add " />
</form>

</div>