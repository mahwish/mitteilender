<%inherit file="base.mako"/>
 <h1>Project Name : ${project_name}
  <br /><br />
Add File Item    </h1>
  <br /><br /><br />
<div>
   
                    <form action="${request.route_url('upload_f', pname=project_name)}" method="POST" enctype="multipart/form-data">
                    
                   Item Name<input type="text" name="name" value="" required /><br /><br /><br />
   

 



 
      
      
        
                     
                        <input type="file" name="csv_file"required />
                        <br /><br />
                        <input type="submit" value="upload" />
                    </form>
                
                    
                &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=project_name)}"><font color="teal"><b>Back</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        
</div>
