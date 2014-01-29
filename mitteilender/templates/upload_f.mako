<%inherit file="base.mako"/>
<<<<<<< HEAD
 <h1>Project Name : ${project_name}
  <br /><br />
Add File Item    </h1>
=======
  <h1>Upload Csv file - Csv files in Project: ${project_name}</h1>
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
  <br /><br /><br />
<div>
   
                    <form action="${request.route_url('upload_f', pname=project_name)}" method="POST" enctype="multipart/form-data">
                    
<<<<<<< HEAD
                   Item Name<input type="text" name="name" value="" required /><br /><br /><br />
=======
                   Item Name<input type="text" name="name" value=""  /><br /><br /><br />
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
   

 

<<<<<<< HEAD


 
      
      
        
                     
                        <input type="file" name="csv_file"required />
                        <br /><br />
=======
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
                         
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
                        <input type="submit" value="upload" />
                         <input type="hidden" name="item_id" value="${f.pi_id}" />
                    </form>
<<<<<<< HEAD
                
                    
                &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=project_name)}"><font color="teal"><b>Back</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        
</div>
=======
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
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
