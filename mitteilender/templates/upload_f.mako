<%inherit file="base.mako"/>
  <h1>Upload Csv file - Csv files in Project: ${project_name}</h1>
  <br /><br /><br />
<div>
   
                    <form action="${request.route_url('upload_f', pname=project_name)}" method="POST" enctype="multipart/form-data">
                    
                   Item Name<input type="text" name="name" value=""  /><br /><br /><br />
   

 



 
      
         Parent Item<input type="text" name="p_item"  value=""  /><br /><br /><br />
        
                     
                        <input type="file" name="csv_file" />
                        <input type="submit" value="upload" />
                    </form>
                
                    
               
        
</div>
