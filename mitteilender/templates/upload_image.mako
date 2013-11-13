<%inherit file="base.mako"/>

<div>
    <h1>Upload Image - Image Items in Project: ${project.name}</h1>
    <table>
        <tr class="tr_heading">
            <th>Item name</th>
            <th>Value</th>
            <th>Parent Item</th>
            <th>Upload</th>
            <th>Current Image</th>
        </tr>
        %for I in image_items:
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td>${I.item_name}</td>
                <td>${I.item_value}</td>
                <td>${I.parent_item}</td>
                <td>
                    <form action="${request.route_url('upload_image', pname=project.name)}" method="POST" enctype="multipart/form-data">
                        <input type="hidden" name="item_id" value="${I.pi_id}" />
                        <input type="file" name="image_file" />
                        <input type="submit" value="upload" />
                    </form>
                </td>
                <td>
                    <img src="${request.static_url('mitteilender:static/uploaded_images/%i.jpg' % I.pi_id)}" height="50" width="50"
                </td>
            </tr>
        %endfor
        
    </table>
</div>