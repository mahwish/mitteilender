<%inherit file="base.mako"/>

<%def name="title()">


</%def>

<div>
<h1>Add User Input</h1>
<form action="${request.route_url('inputs/new',item_id=item_id)}" method="POST">
  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  ${add_input.as_p() | n}
    <input type="submit" name="form.submitted" value="Add Input" />
</form>
<br /><br /><br /><br /><br /><br />
</div>