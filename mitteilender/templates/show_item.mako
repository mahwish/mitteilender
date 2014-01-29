<%inherit file="base.mako"/>

<div>
    <h1>Projects Items</h1>
   %for data in item_data:
   
       %if (data.item_type=='Text'):
       Item Name:
   <input type="text" value=${data.item_name} />
     <br /><br /><br />
    Item Value:
   <textarea > ${data.item_value} </textarea>
     <br /><br /><br />
    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('text_item', pname=pname)}"><font color="teal"><b>Add another Item</a>
  
   %endif
    %if (data.item_type=='Section'):
       Item Name:
   <input type="text" value=${data.item_name} />
     <br /><br /><br />
     
     &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('section_item', pname=pname)}"><font color="teal"><b>Add another Item</a>
    
   %endif
    %if (data.item_type=='Email'):
       Item Name:
   <input type="text" value=${data.item_name} />
     <br /><br /><br />
    Item Value:
   <input type="text" value=${data.item_value} />
    <br /><br /><br />
     &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('email', pname=pname)}"><font color="teal"><b>Add another Item</a>
       
   %endif
    %if (data.item_type=='Contact'):
       Item Name:
   <input type="text" value=${data.item_name} />
     <br /><br /><br />
    Item Value:
     <input type="text" value=${data.item_value} />
   %endif
   
    

  %endfor
  
  
     <br /><br /><br />
  
  
  
  
  
  
  
      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=pname)}"><font color="teal"><b>Back to Add items Item</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
  
</div> 



 