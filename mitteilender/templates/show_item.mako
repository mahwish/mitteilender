<%inherit file="base.mako"/>

<div>
    <h1>Projects Items</h1>
<<<<<<< HEAD
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
  
=======
    <table>
        <tr class="tr_heading">
            <th>Item ID</th>
            <th>Item Name</th>
            <th>Item Type</th>
            <th>Item Values</th>
            <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbspActions</th>
        </tr>
        
       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
       %for I in image_data:
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td>${I.pi_id}</td>
                <td>${I.item_name}</td>
                <td>${I.item_type}</td>
                <td>${I.item_value}</td>
               
                <td>
                 
                   
                  
                   
                   
                </td>
            </tr>
        %endfor
        
    </table>
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
</div> 



 