<%inherit file="base.mako"/>
  <h1>Upload Image Item - Csv files in Project: ${project_name}</h1>
<div>
   
                    <form action="${request.route_url('upload_image', pname=project_name)}" method="POST" enctype="multipart/form-data">
                                <br /><br /><br /> 
                   Item Name<input type="text" name="name" value=""  /><br /><br /><br />
   

 



 
      

        
                     
                        <input type="file" name="image_file" />
                      
                        
                        
                        <br /><br /><br />
                        
       
      
          Parent Item
        <select name=p_item>




%for i in parent_item:

 <option name=${i['sec_id']} value=${i['sec_id']} >${i['sec_name']}</option>
 

 %endfor
  </select>
  
    <input type="submit" value="upload" />
                    </form>
                
                    
               
        
</div>