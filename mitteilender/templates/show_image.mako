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
     &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('upload_image', pname=pname)}"><font color="teal"><b>Add another Image </a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
      &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  <a href="${request.route_url('add', pname=pname)}"><font color="teal"><b>Back to Add items Item</a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
  

</div> 



 