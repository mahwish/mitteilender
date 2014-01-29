<%inherit file="base.mako"/>
<<<<<<< HEAD
  <h1>Project Name : ${project_name}
  <br /><br />
Add Image Item    </h1>
=======
  <h1>Upload Image Item - Csv files in Project: ${project_name}</h1>
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
<div>
   
                    <form action="${request.route_url('upload_image', pname=project_name)}" method="POST" enctype="multipart/form-data">
                                <br /><br /><br /> 
<<<<<<< HEAD
                   Item Name<input type="text" name="name" value=""required  /><br /><br /><br />
=======
                   Item Name<input type="text" name="name" value=""  /><br /><br /><br />
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
   

 



 
      

        
                     
<<<<<<< HEAD
                        <input type="file" name="image_file" required />
=======
                        <input type="file" name="image_file" />
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
                      
                        
                        
                        <br /><br /><br />
                        
<<<<<<< HEAD
     %if (parent_item==[]):
       Parent item : 
       None
       
     
      %else:
      Parent item:
     <select name=p_item>
=======
       
      
          Parent Item
        <select name=p_item>
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b




%for i in parent_item:

<<<<<<< HEAD

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
              
=======
 <option name=${i['sec_id']} value=${i['sec_id']} >${i['sec_name']}</option>
 

 %endfor
  </select>
  
    <input type="submit" value="upload" />
                    </form>
                
                    
               
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
        
</div>