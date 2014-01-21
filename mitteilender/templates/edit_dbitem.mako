    <%inherit file="base.mako"/>

<div>
    <h1>EDit DB Item</h1>
    <br /><br /><br />
 <form action="${request.route_url('edit_dbitem',item_id=item_id,dbitem_id=dbitem_id, rec_id=rec_id)}" method="POST" enctype="multipart/form-data">
 
                     

<br /><br /><br />
        
     
        %for i in rec_value:
    
    
     <input type="text" name=${i['value']}  value=${i['value']}>
     <input type="hidden" name=${i['did']}  value=${i['value']}>
       <input type="hidden" name=${i['rid']}  value=${i['value']}>
     
     <br /><br /><br />
   
<br /><br /><br />
 %endfor
 </input>
   
 
   <input type="submit" name="form.submitted" value="Done" />
</form>



