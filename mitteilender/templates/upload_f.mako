<%inherit file="base.mako"/>
  <h1>Upload Csv file - Csv files in Project: ${project_name}</h1>
  <br /><br /><br />
<div>
   
                    <form action="${request.route_url('upload_f', pname=project_name)}" method="POST" enctype="multipart/form-data">
                    
                   Item Name<input type="text" name="name" value=""  /><br /><br /><br />
   

 

<<<<<<< HEAD


=======

<<<<<<< HEAD

>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
 
      
         Parent Item<input type="text" name="p_item"  value=""  /><br /><br /><br />
        
                     
<<<<<<< HEAD
=======
=======
    <h1>Upload Csv file - Csv files in Project: ${project.name}</h1>
    <table>
     <td>
       %for f in f_items:
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td>${f.item_name}</td>
                <td>${f.item_value}</td>
                <td>${f.parent_item}</td>
                <td>
                    <form action="${request.route_url('upload_f', pname=project.name)}" method="POST" enctype="multipart/form-data">
                        
>>>>>>> bcea36c4043c05d26b70fceef21c71b44940e14f
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
                        <input type="file" name="csv_file" />
                         
                        <input type="submit" value="upload" />
                         <input type="hidden" name="item_id" value="${f.pi_id}" />
                    </form>
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
                
                    
               
        
</div>
<<<<<<< HEAD
=======
=======
                </td>
             %endfor
        <tr class="tr_heading">
        %for f in fields:
        <th>${f}</th>
        %endfor
            
        </tr>
        %for r in records:
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                %for item in r:
                <td>${item}</td>
                %endfor
            </tr>
        %endfor
    </table>
</div> 
>>>>>>> bcea36c4043c05d26b70fceef21c71b44940e14f
>>>>>>> 5b7b1152fb27074d2bd0aae1b196b4dfa2e15332
