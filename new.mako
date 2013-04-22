<%inherit file="base.mako"/>

<%def name="title()">
PyCK Project - Contact Us
</%def>
      <div class="middle align-center">
        <p><font color="teal"><b>
<div>
<h1>New Project</h1>

<form action="${request.route_url('new')}" method="POST">
    ${new_form.as_p() | n}
    <input type="submit" name="form.submitted" value="Create" />
</form>

<br /><br /><br /><br /><br /><br />
</div> 
