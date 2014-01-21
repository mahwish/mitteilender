<%inherit file="base.mako"/>

<div>
    <h1>Projects Items</h1>
       <form action="${request.route_url('swap_display_order', p_id=p_id)}" method="POST">
                                <br /><br /><br /> 
    <table>
        <tr class="tr_heading">
            <th>Item ID</th>
            <th>Item Name</th>
            
             <th>Display Order</th>
              <th>&nbsp&nbsp&nbsp&nbsp&nbspSwap</th>
         
            
        </tr>
        
       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
       %for I in p_items:
       
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td>${I.pi_id}</td>
                <td>${I.item_name}</td>
           
                <td>&nbsp&nbsp&nbsp&nbsp&nbsp${I.display_order}</td> 
               
               
               
               
                <td>
                <select name=${I.pi_id}
               
                %if (I.pi_id==first):
                 <option value="down">down</option>
                 <option value="No change">No change</option>
                
                 %elif (I.pi_id==last):
                 
                <option value="up">up</option>
              <option value="No change">No change</option>
                %else:
           
                 <option value="up">up</option>
                 <option value="down">down</option>
                <option value="No change">No change</option>
                  
         %endif
     
                </select>
             
             
            </td>
           
        %endfor
      <tr>
  
     
   </tr>   
    </table>
</div> 
<input type="submit" value="Change" />
</form>


 