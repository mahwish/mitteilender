<%inherit file="base.mako"/>

<%def name="title()">


</%def>

<div>
<<<<<<< HEAD
<h1>Add User Input</h1>
<form action="${request.route_url('inputs/new',item_id=item_id)}" method="POST">
=======
<h1>Add User Input/h1>
<form action="${request.route_url('new_input',item_id=item_id)}" method="POST">
>>>>>>> 58e0521f5282513e432016741fbe067bf9fb781b
  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  ${add_input.as_p() | n}
    <input type="submit" name="form.submitted" value="Add Input" />
</form>
<br /><br /><br /><br /><br /><br />
</div>