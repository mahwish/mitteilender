<%inherit file="base.mako"/>

<div>
<br>
<br>
<br>



<h1><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u>LIST OF ALL PROJECTS</u></b></h1>
<br>
<br>
<br>
<table>
<tr>
<th width="50">&nbsp;ID</th>
<th width="140">NAME&nbsp;&nbsp; </th>

<th width="150">&nbsp;&nbsp;DESCRIPTION</th>
</tr>
</table>
%for category in plist:
<table>
<tr>
<td width="50">
<h3>&nbsp;&nbsp;&nbsp;${category.ip_id}</h3>
</td>
<td width="200">
<h3>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;${category.name}</h3>
</td>
<td width="120">
<h3>&nbsp;&nbsp;&nbsp;${category.ip_description}&nbsp;&nbsp;&nbsp;</h3>
</td>




</tr>


%endfor
</table>


        
        
    
   

<br>
<br>
<br>
<br>
<br>
<br> 
