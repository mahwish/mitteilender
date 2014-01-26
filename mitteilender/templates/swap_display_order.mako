<%inherit file="base.mako"/>

<div>
    <h1>Projects Items</h1>
     
                                <br /><br /><br /> 
    <table>
        <tr class="tr_heading">
            <th>Item Name</th>
            
             <th>Display Order</th>
              <th>&nbsp&nbsp&nbsp&nbsp&nbspSwap</th>
         
            
        </tr>
        
       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
       %for I in p_items:
       
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
               
               
                <td>${I.item_name}</td>
           
                <td>&nbsp&nbsp&nbsp&nbsp&nbsp${I.display_order}</td> 
               
               
               
               
                <td>
              
               
               
                
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
     
           
             
             
            </td>
           
        %endfor
      <tr>
  
     
   </tr>   
    </table>
</div> 

</form>


 