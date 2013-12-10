<%inherit file="base.mako"/>

<div>

    <h1>Upload Csv file - Csv files in Project: ${project.name}</h1>
    <table>
     <td>
                    <form action="${request.route_url('upload_f', pname=project.name)}" method="POST" enctype="multipart/form-data">
                        
                        <input type="file" name="csv_file" />
                        <input type="submit" value="upload" />
                    </form>
                </td>
        
        <tr class="tr_heading">
        %for f in fields:
        <th>${f}</th>
        %endfor
            
        </tr>
        %for r in records:
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                %for item in r:
                <td>${item}</td>
                %endfor
            </tr>
        %endfor
    </table>
</div> 
