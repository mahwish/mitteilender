<%inherit file="base.mako"/>
<br /><br />
<div>
<h1>Data Items of .csv file</h1>
<br /><br />
%for row in reader:
		%for col in row:
			${col}&nbsp&nbsp
			%endfor
		<br></br>
		%endfor
<br /><br /><br /><br /><br /><br /><br /><br /><br />	
</div>
