<%inherit file="base.mako"/>

<%def name="title()">
PyCK Project - More Items
</%def>
      <div class="middle align-center">
        <p><font color="teal"><b>
<div>
<h1>More Items</h1>

<form action="${request.route_url('more_items')}" method="POST">
    ${more_items_form.as_p() | n } <br><br><br>
    <input type="submit" name="form.submitted" value="Upload" />
</form>

<br /><br /><br /><br /><br /><br />
</div> 
 
