 
<%inherit file="base.mako"/>

<div>
    <h1>Upload File - File Items in Project: ${project.name}</h1>
    <table>
        <tr class="tr_heading">
            <th>Item name</th>
            <th>Value</th>
            <th>Parent Item</th>
            <th>Upload</th>
            <th>Current File</th>
        </tr>
        %for k in file_items:
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td>${k.item_name}</td>
                <td>${k.item_value}</td>
                <td>${k.parent_item}</td>
                <td>
                    <form action="${request.route_url('upload_file', pname=project.name)}" method="POST" enctype="multipart/form-data">
                        <input type="hidden" name="item_id" value="${k.pi_id}" />
                        
                        <input type="file" name="upload_file" />
                        <input type="submit" value="upload" />
                    </form>
                </td>
                <td>
                    <img src="${request.static_url('mitteilender:static/uploaded_files/%i.csv' % k.pi_id)}" height="50" width="50"
                </td>
            </tr>
        %endfor
        
    </table>
</div>