
  
<%inherit file="base.mako"/>
<div>
    <h1>Projects Items</h1>
    <table>
        <tr class="tr_heading">
            <th>Item ID</th>
            <th>Item Name</th>
            <th>Item Type</th>
            <th>Item Values</th>
             <th>Display Order</th>
              <th>&nbsp&nbsp&nbsp&nbsp&nbspSwap</th>
              <th>&nbsp&nbsp&nbsp&nbsp&nbspParent Item</th>
            <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbspActions</th>
        </tr>
        
       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
       %for I in p_items:
       
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td>${I.pi_id}</td>
                <td>${I.item_name}</td>
                <td>${I.item_type}</td>
                <td>${I.item_value}</td>
                <td>&nbsp&nbsp&nbsp&nbsp&nbsp${I.display_order}</td> 
                 <td>ppppppppp</td>
                <td>&nbsp&nbsp&nbsp&nbsp&nbsp${I.parent_item}</td>
               
                <td>
           
                  
                   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('del_item', item_id=I.pi_id)}"><font color="teal"><b>Delete Item</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<a href="${request.route_url('edit_item', item_id=I.pi_id)}"><font color="teal"><b>Edit Item</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<a href="${request.route_url('swap_display_order', p_id=I.infoproject_id)}"><font color="teal"><b>Change Disply order </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                     
                    %if (I.item_type=='Image'):
                    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('show_image', item_id=I.pi_id)}"><font color="teal"><b>Show Image</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                    %endif
                   
                  %if (I.item_type=='DbItem'):
                    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('show_dbitem', item_id=I.pi_id)}"><font color="teal"><b>Show DB Item</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('field_type', item_id=I.pi_id)}"><font color="teal"><b>Edit Field Type</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('primary_display', item_id=I.pi_id)}"><font color="teal"><b>Set Primary Display Field</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                     &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('del_dbitem', item_id=I.pi_id)}"><font color="teal"><b> Delete table record</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                     &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('new_input', item_id=pname)}"><font color="teal"><b> Add Input </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                    %endif
                
                   
                   
                </td>
            </tr>
        %endfor
        
    </table>
</div> 



 