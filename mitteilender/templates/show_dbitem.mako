<%inherit file="base.mako"/>

<div>
    <h1>Projects Item</h1>
    
    <table>
        <tr class="tr_heading">
        %for name in f_name:
            <th>${name}</th>
            <th>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th>
           
     
       
         
     
           %endfor
           
           
           
            </tr>
            
            
             
        %for i in f_value:
         <tr class="tr_heading">
        %for ii in i:
        
            <td>${ii}</td>
           
     <td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
       
         
     
           %endfor
           
        
           
            </tr>
    %endfor
    </table>
       <br /><br /><br />
    <FORM><INPUT Type="button" VALUE="Back" width="50px" onClick="history.go(-1);return true;"></FORM>
</div> 



 