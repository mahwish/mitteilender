<%inherit file="base.mako"/>

<div>
    <h1>Add Project Item</h1>
    <br /><br /><br />
    
  %if (type=='email'):
  
   
    
 <form action="${request.route_url('edit_item',item_id=item_id)}" method="POST">

<br /><br /><br />
      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  ${email_form.as_p() | n}
    <input type="submit" name="form.submitted" value="edit Item" />
</form>
%endif


%if (type=='image'):
  
   
    
 <form action="${request.route_url('edit_item',item_id=item_id)}" method="POST" enctype="multipart/form-data">
 
                        <input type="file" name="image" />
                        <input type="submit" value="upload" />

<br /><br /><br />
       Item Name<input type="text" name="name" value=${data.item_name}  /><br /><br /><br />
       
        Display Order<input type="text"  name="d_order" value=${data.display_order} /><br /><br /><br />
         Parent Item<input type="text" name="p_item"  value=${data.parent_item}  /><br /><br /><br />  
<br /><br /><br />
 
   
</form>
%endif


%if (type=='dbitem'):
  
   
    
 
 
               

<br /><br />
  <table>
        <tr class="tr_heading">
      
            <th>DB rec Id</th>
            <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
            <th>DB item Id</th>
            <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
          <th>DB Value</th>
            <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
            <th>DB Actions</th>
            <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
      
     </tr> 
     %for i in f_value:
      
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
      
            <td>${i['d_id']}</td>
                 <td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
             <td>${i['dbitem_id']}</td>
                  <td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
              <td>${i['db_rec']}</td>
             
         <td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
                 
             <td><a href="${request.route_url('edit_dbitem', item_id=item_id, dbitem_id=i['dbitem_id'], rec_id=i['d_id'])}"><font color="teal"><b>Edit Row</a></td>   
         
     
           
      
        
             
           
           
            </tr>
    %endfor
<br /><br /><br />
 
   </table>

%endif


</div>



 