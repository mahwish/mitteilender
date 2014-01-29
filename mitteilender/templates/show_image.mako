<%inherit file="base.mako"/>

<div>
    <h1>Image Item</h1>
    <table>
      <td>
      Image:
      <img border="0" src=${path} alt="Image loading problem" width="304" height="228"></image>
      
                </td>
                <tr>
            </tr>
     
        
    </table>
    <br /><br /><br />
<<<<<<< HEAD
     &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('upload_image', pname=pname)}"><font color="teal"><b>Add another Image </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=pname)}"><font color="teal"><b>Back to Add items Item</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
  
=======
  <FORM><INPUT Type="button" VALUE="Back" width=50px onClick="history.go(-1);return true;"></FORM>
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b

</div> 



 