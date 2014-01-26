<%inherit file="base.mako"/>
<%inherit file="home.mako"/>

<div>
    <h1>Projects List</h1>
    <table>
        <tr class="tr_heading">
            <th>Project ID</th>
            <th>Project Name</th>
            <th>Description</th>
            <th>Actions</th>
        </tr>
        
       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
       %for P in projects:
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td>${P.ip_id}</td>
                <td>${P.name}</td>
                <td>${P.ip_description}</td>
                <td>
                   
                     <a href="${request.route_url('view_items', pname=P.name)}"><font color="teal"><b>View Items</a>
                      <a href="${request.route_url('add', pname=P.name)}"><font color="teal"><b>Add Item</a>
                   
                </td>
            </tr>
        %endfor
        
    </table>
</div>