<%inherit file="base.mako"/>






 
<<<<<<< HEAD
 
=======
 Input Type : Open
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
  <br /><br /><br />
   <tr class="tr_heading">

   %for v in values:
   %if (v['type']=='open'):
<<<<<<< HEAD
   Input Type : Open
  
=======
   
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
   
 

<td>  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" value=${v['name']} ></td>
<br /><br /><br />
%endif


  %if (v['type']=='single_select'):
<<<<<<< HEAD
   Input Type : Single Select
  
=======
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
   
   
 

<td>  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td><input type="radio"  value=${v['name']}>${v['name']}</td>
<br /><br /><br />
%endif

  %if (v['type']=='multi_select'):
   
   
<<<<<<< HEAD
 Input Type : Multiselect
  
=======
 
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b

<td>  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="checkbox" value=${v['name']} >${v['name']}</td>
<br /><br /><br />
%endif
</tr>

%endfor


</td>

<td> 
 

                   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('new_input', item_id=p_id)}"><font color="teal"><b>Add new input Item </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<<<<<<< HEAD
                   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('input_manage', item_id=p_id,input_id=input_id)}"><font color="teal"><b>Add more fields </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                     &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('p_list')}"><font color="teal"><b>Done  </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp

=======
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b




