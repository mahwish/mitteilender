<%inherit file="base.mako"/>

<div>
    <h1>Projects Items</h1>
<<<<<<< HEAD
     
                                <br /><br /><br /> 
    <table>
        <tr class="tr_heading">
=======
       <form action="${request.route_url('swap_display_order', p_id=p_id)}" method="POST">
                                <br /><br /><br /> 
    <table>
        <tr class="tr_heading">
            <th>Item ID</th>
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
            <th>Item Name</th>
            
             <th>Display Order</th>
              <th>&nbsp&nbsp&nbsp&nbsp&nbspSwap</th>
         
            
        </tr>
        
       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
       %for I in p_items:
       
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
<<<<<<< HEAD
               
               
=======
                <td>${I.pi_id}</td>
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
                <td>${I.item_name}</td>
           
                <td>&nbsp&nbsp&nbsp&nbsp&nbsp${I.display_order}</td> 
               
               
               
               
                <td>
<<<<<<< HEAD
              
               
               
                
                 %if (I.display_order==last):
                  
<a href="${request.route_url('swap', item_id=I.pi_id, direction='up')}">
<img width="50px" height="20px" src="${request.static_url('mitteilender:static/up.jpeg')}"></a>

              
               %elif (I.display_order==first):
                  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp   &nbsp&nbsp&nbsp&nbsp&nbsp   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                 <a href="${request.route_url('swap', item_id=I.pi_id, direction='down')}">
                 <img  width="50px" height="20px"
                 src="${request.static_url('mitteilender:static/down.jpeg')}"></a>
              
                %else:
           
                 <a href="${request.route_url('swap', item_id=I.pi_id, direction='up')}">
                 <img width="50px" height="20px" src="${request.static_url('mitteilender:static/up.jpeg')}"></a>
              
                    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                     <a href="${request.route_url('swap', item_id=I.pi_id, direction='down')}">
                     <img width="50px" height="20px" src="${request.static_url('mitteilender:static/down.jpeg')}"></a>
              
         %endif
     
           
=======
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
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
             
             
            </td>
           
        %endfor
      <tr>
  
     
   </tr>   
    </table>
</div> 
<<<<<<< HEAD

=======
<input type="submit" value="Change" />
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
</form>


 