    <%inherit file="base.mako"/>

<div>
    <h1>EDit DB Item</h1>
    <br /><br /><br />
 
<form action="${request.route_url('del_dbitem',item_id=item_id)}" method="POST" enctype="multipart/form-data">                     

<br /><br /><br />
          
      
       <table>
        <tr class="tr_heading">
        %for name in f_name:
        <th></th>
            <th>${name}</th>
            <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
           
     
       
         
     
           %endfor
           
           
           
            </tr>
            
            
             
        %for i in range(len(f_value)):
        %for j in range(len(idz)): 
        
        %if (i==j):
         <tr class="tr_heading">
        <td> <input type="hidden" name=i  value=${idz[j]} /></td>
        %for ii in f_value[i]:
        
        
            <td>${ii}&nbsp&nbsp&nbsp&nbsp</td>
           
     <td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
      
           %endfor
           <td>   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('del_rec', item_id=item_id, rec_id=idz[j])}"><font color="teal"><b>Delete record </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>   
        %endif
           
    %endfor
     
   
         %endfor
            </tr>
   
    </table>
    
     <br /><br /><br />
   
<br /><br /><br />
 
 </form>   </tr>

  <br /><br /><br />
  <FORM><INPUT Type="button" VALUE="Back" width=50px onClick="history.go(-1);return true;"></FORM>
