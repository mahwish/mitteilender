<%inherit file="base.mako"/>

<%def name="title()">
Project : ${project_name}
</%def>

<div>
<h1>Contact Us</h1>
<form action="${request.route_url('email',pname=project_name)}" method="POST">
  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  ${add_email.as_p() | n}
    <input type="submit" name="form.submitted" value="Add Item" />
</form>
<br /><br /><br /><br /><br /><br />
</div>