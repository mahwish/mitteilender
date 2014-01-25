<%inherit file="base.mako"/>

<div>
    <h1>Projects Items</h1>
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
</div> 



 