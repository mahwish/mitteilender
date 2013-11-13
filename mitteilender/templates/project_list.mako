<%inherit file="base.mako"/>

<div>
    <h1>Projects List</h1>
    <table>
        <tr class="tr_heading">
            <th>Project ID</th>
            <th>Project Name</th>
            <th>Description</th>
            <th>Actions</th>
        </tr>
        %for P in projects:
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td>${P.ip_id}</td>
                <td>${P.name}</td>
                <td>${P.ip_description}</td>
                <td>
                    <a href="">View Items</a> |
                    <a href="${request.route_url('upload_image', pname=P.name)}">Upload Image</a>
                </td>
            </tr>
        %endfor
        
    </table>
</div>