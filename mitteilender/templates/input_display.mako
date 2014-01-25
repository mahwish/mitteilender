<%inherit file="base.mako"/>






 
 Input Type : Open
  <br /><br /><br />
   <tr class="tr_heading">

   %for v in values:
   %if (v['type']=='open'):
   
   
 

<td>  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" value=${v['name']} ></td>
<br /><br /><br />
%endif


  %if (v['type']=='single_select'):
   
   
 

<td>  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td><input type="radio"  value=${v['name']}>${v['name']}</td>
<br /><br /><br />
%endif

  %if (v['type']=='multi_select'):
   
   
 

<td>  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="checkbox" value=${v['name']} >${v['name']}</td>
<br /><br /><br />
%endif
</tr>

%endfor


</td>

<td> 
 

                   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('new_input', item_id=p_id)}"><font color="teal"><b>Add new input Item </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp




