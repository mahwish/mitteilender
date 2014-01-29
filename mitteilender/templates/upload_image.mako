<%inherit file="base.mako"/>
  <h1>Project Name : ${project_name}
  <br /><br />
Add Image Item    </h1>
<div>
   
                    <form action="${request.route_url('upload_image', pname=project_name)}" method="POST" enctype="multipart/form-data">
                                <br /><br /><br /> 
                   Item Name<input type="text" name="name" value=""required  /><br /><br /><br />
   

 



 
      

        
                     
                        <input type="file" name="image_file" required />
                      
                        
                        
                        <br /><br /><br />
                        
     %if (parent_item==[]):
       Parent item : 
       None
       
     
      %else:
      Parent item:
     <select name=p_item>




%for i in parent_item:


 <option name=${i['sec_id']} value=${i['sec_id']} >${i['sec_name']}</option>

 

 %endfor
  <option name=${i['sec_id']} value='None' >None</option>
  </select>
  %endif
      <br /><br /><br />
    <input type="submit" value="upload" />
                    </form>
       
        <br /><br /><br />
                    
    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=project_name)}"><font color="teal"><b>Back</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
              
        
</div>